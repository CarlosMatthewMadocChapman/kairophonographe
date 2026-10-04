from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CANON = ROOT / "canon"


def _load(name: str) -> dict[str, Any]:
    return json.loads((CANON / name).read_text(encoding="utf-8"))


def _band(value: float | None, bands: list[dict[str, Any]]) -> dict[str, Any] | None:
    if value is None:
        return None
    for band in bands:
        lower_ok = "min" not in band or value >= band["min"]
        upper_ok = "max" not in band or value < band["max"]
        if lower_ok and upper_ok:
            return band
    return None


def _time_period(hour: int, mapping: dict[str, Any]) -> dict[str, Any]:
    for period in mapping["periods"]:
        if hour in period["hours"]:
            return period
    raise ValueError(f"No time period for hour {hour}")


def _clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def translate(session: dict[str, Any]) -> dict[str, Any]:
    weather_map = _load("weather_mapping.json")
    time_map = _load("time_mapping.json")
    season_map = _load("season_mapping.json")
    geology_map = _load("geology_mapping.json")
    sound_map = _load("sound_mapping.json")
    place_map = _load("place_mapping.json")
    music_map = _load("music_mapping.json")
    vocal_map = _load("vocality_mapping.json")
    anti_map = _load("anti_recycling.json")

    inp = session["input"]
    w = inp["weather"]
    snd = inp["sound"]
    place = inp["place"]

    t_band = _band(w.get("temperature_c"), weather_map["variables"]["temperature_c"]["bands"])
    h_band = _band(w.get("humidity_pct"), weather_map["variables"]["humidity_pct"]["bands"])
    p_band = _band(w.get("pressure_hpa"), weather_map["variables"]["pressure_hpa"]["bands"])
    wind_band = _band(w.get("wind_speed_kmh"), weather_map["variables"]["wind_speed_kmh"]["bands"])
    rain_band = _band(w.get("precipitation_mm_h"), weather_map["variables"]["precipitation_mm_h"]["bands"])
    cloud_band = _band(w.get("cloud_cover_pct"), weather_map["variables"]["cloud_cover_pct"]["bands"])
    period = _time_period(inp["time"]["local_hour"], time_map)
    season = season_map["seasons"][inp.get("season", "unknown")]

    tempo = float(music_map["base_tempo_bpm"])
    for band in (t_band, wind_band, rain_band):
        if band:
            tempo += float(band.get("tempo_bias_bpm", 0))
    tempo += (float(snd.get("event_density", 0.5)) - 0.5) * 16
    tempo += float(period.get("density_bias", 0)) * 10
    tempo += float(season.get("density_bias", 0)) * 8
    lo, hi = music_map["tempo_limits_bpm"]
    tempo = round(_clamp(tempo, lo, hi), 1)

    density = 0.35 + 0.45 * float(snd.get("event_density", 0.5))
    if rain_band:
        density += 0.20 * float(rain_band.get("event_density", 0))
    density += float(period.get("density_bias", 0))
    density += float(season.get("density_bias", 0))
    density = round(_clamp(density, 0.05, 0.95), 2)

    place_rule = place_map["place_types"].get(place.get("type"), place_map["place_types"]["other"])
    palettes = place_rule["eligible_palettes"][:]

    # Add material/weather-driven palette candidates without duplicates.
    if h_band and h_band.get("layer_fusion", 0) >= 0.60:
        palettes += ["Halos humides"]
    if wind_band and wind_band.get("stereo_motion", 0) >= 0.60:
        palettes += ["Stéréo mouvante"]
    if rain_band and rain_band.get("event_density", 0) >= 0.50:
        palettes += ["Percussions humides", "Ostinatos liquides"]
    palettes = list(dict.fromkeys(palettes))[:3]

    timbres: list[str] = []
    for material in place.get("geology", []) + place.get("materials", []):
        rule = geology_map["materials"].get(material)
        if rule:
            timbres.extend(rule["timbres"])
    timbres = list(dict.fromkeys(timbres))[:6]

    sound_roles: list[str] = []
    vocal_candidates: list[str] = []
    for family in snd.get("families", []):
        rule = sound_map["source_families"].get(family)
        if not rule:
            continue
        sound_roles.extend(rule["music_roles"])
        vt = rule.get("vocal_transmutation", {})
        threshold = vt.get("min_source_density")
        if inp.get("vocality_allowed", True) and vt.get("eligible") and threshold is not None and snd.get("event_density", 0) >= threshold:
            vocal_candidates.append(vt["mode"])

    # Kinetic regime is an interpretable deterministic arbitration.
    periodicity = float(snd.get("periodicity", 0.0))
    variability = float(snd.get("dynamic_variability", 0.0))
    wind = float(w.get("wind_speed_kmh") or 0)
    rain = float(w.get("precipitation_mm_h") or 0)
    if rain >= 1 or wind >= 20:
        kinetic = "active_weather"
    elif "machines" in snd.get("families", []) and periodicity >= 0.45:
        kinetic = "living_mechanical"
    elif "human_steps" in snd.get("families", []) or periodicity >= 0.60:
        kinetic = "walking_ostinato"
    elif variability >= 0.75:
        kinetic = "montage_rupture"
    elif snd.get("event_density", 0) <= 0.25:
        kinetic = "contemplative_breathed"
    else:
        kinetic = "place_song" if vocal_candidates else "social_polyrhythmic"

    tempo_range = music_map["kinetic_regimes"][kinetic]["tempo_range"]
    tempo = round(_clamp(tempo, tempo_range[0], tempo_range[1]), 1)

    quarantined = []
    haystack = " ".join([session.get("intent", ""), session.get("location", {}).get("name", ""), session.get("session_id", ""), place.get("type", ""), *place.get("materials", []), *place.get("visual_forces", [])]).lower()
    for motif in anti_map["quarantined_reference_motifs"]:
        if motif.lower() in haystack:
            quarantined.append(motif)

    return {
        "session_id": session["session_id"],
        "engine_version": session["engine_version"],
        "music_spec": {
            "tempo_bpm": tempo,
            "density": density,
            "kinetic_regime": kinetic,
            "structural_mode": period["structural_mode"],
            "register_bias": period["register_bias"],
            "seasonal_orchestration": season["orchestration"],
            "space_decay_s": h_band.get("space_decay_s") if h_band else None,
            "stereo_motion": wind_band.get("stereo_motion") if wind_band else None,
            "harmonic_gravity": p_band.get("harmonic_gravity") if p_band else None,
            "spectral_brightness": cloud_band.get("spectral_brightness") if cloud_band else None,
            "palettes": palettes,
            "timbres": timbres,
            "sound_roles": list(dict.fromkeys(sound_roles)),
            "vocality": vocal_candidates[0] if vocal_candidates else vocal_map["modes"]["0"],
            "source_preservation_rule": "Keep recognizable timing, contour, density or attack evidence from the situated input."
        },
        "anti_recycling": {
            "detected_reference_motifs": quarantined,
            "requires_explicit_reprise": bool(quarantined)
        },
        "provenance": session["provenance"]
    }

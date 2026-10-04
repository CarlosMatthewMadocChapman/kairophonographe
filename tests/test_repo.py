import json
from pathlib import Path
from jsonschema import Draft202012Validator
from api.engine import translate

ROOT = Path(__file__).resolve().parents[1]


def load(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def test_manifest_version_matches_root():
    assert (ROOT / "VERSION").read_text().strip() == load("canon/manifest.json")["version"]


def test_all_examples_validate():
    schema = load("schemas/session.schema.json")
    validator = Draft202012Validator(schema)
    for path in (ROOT / "examples").glob("*/session.json"):
        assert not list(validator.iter_errors(json.loads(path.read_text(encoding="utf-8")))), path


def test_hot_storm_is_active_weather():
    out = translate(load("examples/la-rousselie/session.json"))
    assert out["music_spec"]["kinetic_regime"] == "active_weather"
    assert out["music_spec"]["density"] >= 0.75


def test_new_terrain_is_not_quarantined():
    out = translate(load("examples/new-terrain/session.json"))
    assert out["anti_recycling"]["detected_reference_motifs"] == []


def test_reference_fixture_triggers_quarantine():
    out = translate(load("examples/karsaka/session.json"))
    assert "Karsaka" in out["anti_recycling"]["detected_reference_motifs"]

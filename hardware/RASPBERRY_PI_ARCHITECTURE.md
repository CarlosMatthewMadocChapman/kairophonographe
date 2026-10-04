# Raspberry Pi acquisition architecture

The hardware layer captures evidence. It should not contain hidden musical logic.

```text
microphone / audio interface ─┐
camera ───────────────────────┤
temperature-humidity-pressure ├─> acquisition service ─> normalized session JSON
wind / rain / light ──────────┤                           │
clock + optional GNSS ────────┘                           └─> reference engine / API
```

## Recommended process separation

1. **Acquire** raw or summarized sensor data.
2. **Timestamp** all samples using one local/UTC clock strategy.
3. **Normalize** units to the public session contract.
4. **Record provenance** for each field.
5. **Reduce location precision** before public export when exact coordinates are unnecessary.
6. **Translate** through the versioned reference engine.
7. **Render** with the chosen sound or music system.
8. **Evaluate** by listening and archive the evaluation separately.

## Interfaces

- audio: USB Audio Class device or supported I2S interface;
- camera: CSI or USB camera;
- environmental sensors: I2C/SPI/GPIO devices producing values in documented units;
- wind/rain: pulse, analog or serial sensors normalized by the acquisition service;
- location: optional GNSS or declared location;
- network: optional, required only for external API weather or remote transport.

## Canonical units

- temperature: °C
- humidity: % RH
- pressure: hPa
- wind speed / gust: km/h
- precipitation rate: mm/h
- cloud cover: %
- timestamp: ISO 8601 with offset
- audio density / periodicity / variability: normalized 0–1 features

## Failure behaviour

Missing sensors produce `null`, never fabricated measurements. The session may still run if enough other forces are available. An estimated or simulated value must be labelled as such in provenance.

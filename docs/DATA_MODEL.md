# Data model

Every value belongs to one of three layers:

### Evidence
Observed or measured values: weather, acoustic features, materials, timestamp, location precision.

### Artistic rule
Versioned mappings from evidence to musical control targets.

### Result
The deterministic music specification and later listening evaluation.

This separation prevents a rendered aesthetic decision from being mistaken for an environmental measurement.

## Claim classes

- `MEASURED` — instrument value with unit and timestamp;
- `OBSERVED` — human/image/audio observation;
- `ARTISTIC_RULE` — explicit mapping chosen by the project;
- `LISTENING_RESULT` — result of evaluation after rendering;
- `HYPOTHESIS` — unvalidated candidate;
- `REFERENCE_EXAMPLE` — reproducible fixture that does not govern new sessions.

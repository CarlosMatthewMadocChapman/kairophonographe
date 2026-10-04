# Reference API

The API exposes the stable mappings and one deterministic translation endpoint.

It does **not** fetch weather, infer GPS, call a music generator or upload media. Acquisition and rendering are deliberately separated from canonical translation so a session can be reproduced later.

## Endpoints

- `GET /health`
- `GET /v1/manifest`
- `GET /v1/mappings/weather_mapping`
- `GET /v1/mappings/time_mapping`
- `GET /v1/mappings/place_mapping`
- `POST /v1/translate`

`POST /v1/translate` validates the session, applies the public mapping rules and returns a music specification suitable for a renderer, prompt composer or live engine.

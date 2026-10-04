# Sensor compatibility contract

Compatibility means a device can supply a value that can be normalized to the session schema. This repository does not require one manufacturer.

| Signal | Expected form | Unit / range | Required? | Public role |
|---|---|---:|---|---|
| Temperature | scalar | °C | no | kinetic/spectral bias |
| Relative humidity | scalar | 0–100 % | no | space/fusion |
| Pressure | scalar | hPa | no | harmonic gravity/stability |
| Wind speed | scalar | km/h | no | spatial motion/modulation |
| Wind gust | scalar/event | km/h | no | punctual events |
| Rain rate | scalar | mm/h | no | density/micro-rhythm |
| Cloud cover | scalar | 0–100 % | no | spectral brightness |
| Camera/image | frame or derived observations | n/a | no | matter/light/shape |
| Audio | PCM/stream or derived features | n/a | strongly recommended | timing/density/source evidence |
| Local time | timestamp | ISO 8601 | yes | structural mode |
| Location | coordinates or declared place | degrees/text | no | context/provenance |

A driver belongs in the acquisition layer. Canonical mappings consume normalized values only.

# Radio du Futur integration

A Kairophonographe session can become a Radio du Futur capsule while preserving the listener's access to the originating moment.

Recommended editorial packet:

1. **raw or minimally processed geo-memory** — a short audible fragment of the source;
2. **situated metadata** — date, local time, publishable location precision, weather provenance and source type;
3. **brief process cue** — one sentence explaining which environmental forces shaped the music;
4. **musical transformation** — the rendered Kairophonographe work;
5. **archive identifier** — session ID and release/mapping version.

The radio layer selects and narrates. It does not rewrite the original session data. A public map can use the same session identifier and reduced location metadata.

## Suggested machine state

```text
CAPTURED → VALIDATED → EDITORIAL_REVIEW → SELECTED → RADIO_READY → PUBLISHED
                                 └──────→ HOLD / PRIVATE / REJECTED
```

The raw source, metadata statement and transformed work should remain separable so the audience can hear the relationship rather than receiving an opaque generated track.

# Reproducibility

A published session should archive:

- session JSON validated against the release schema;
- mapping and engine version;
- acquisition source and units;
- renderer/model/tool version when relevant;
- prompt or score generated from the music specification when publication rights allow it;
- random seed when a downstream renderer uses randomness;
- listening evaluation;
- known limitations.

A strong reproduction test keeps the normalized session fixed and reruns the same translator version. A strong robustness test varies one input family at a time and checks whether the expected musical control family changes.

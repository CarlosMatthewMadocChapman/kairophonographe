# Publication protocol

For a citable release:

1. update `VERSION` and `CHANGELOG.md`;
2. run validation and tests;
3. tag the commit `vX.Y.Z`;
4. create a GitHub Release from that tag;
5. archive the release in a DOI-granting repository if a DOI is desired;
6. keep `CITATION.cff` and `.zenodo.json` aligned with the release;
7. never rewrite an already cited tag.

## Versioning

- **PATCH**: corrections that do not intentionally alter musical outputs for valid sessions;
- **MINOR**: new or modified mappings, schemas or engine behaviour;
- **MAJOR**: incompatible session contract or conceptual model change.

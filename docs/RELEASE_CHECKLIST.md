# Release checklist

- [ ] `VERSION`, `CHANGELOG.md`, `CITATION.cff` and `.zenodo.json` agree.
- [ ] `python scripts/validate_repo.py` passes.
- [ ] `pytest -q` passes.
- [ ] No private GPS, raw private media, credentials or secret tokens are present.
- [ ] New canonical rules have a promotion record and tests.
- [ ] Reference examples are marked with correct provenance.
- [ ] Anti-recycling regression test passes.
- [ ] Git tag is immutable after publication.

# Contributing

Contributions must preserve traceability.

A change to a canonical mapping should include:

1. the rule changed;
2. the source situation or listening evidence that motivated it;
3. at least one regression or evaluation test;
4. known limitations;
5. a version-impact note.

Do not add geographic stereotypes, automatic national styles, untraceable sensor values, private GPS coordinates, copyrighted media or credentials.

Run before proposing a change:

```bash
python scripts/validate_repo.py
pytest -q
```

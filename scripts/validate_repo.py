from __future__ import annotations

import json
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    errors = []

    for path in sorted((ROOT / "canon").glob("*.json")):
        try:
            load(path)
        except Exception as exc:
            errors.append(f"Invalid JSON {path.relative_to(ROOT)}: {exc}")

    schemas = {}
    for path in sorted((ROOT / "schemas").glob("*.json")):
        try:
            schema = load(path)
            Draft202012Validator.check_schema(schema)
            schemas[path.name] = schema
        except Exception as exc:
            errors.append(f"Invalid schema {path.relative_to(ROOT)}: {exc}")

    if "session.schema.json" in schemas:
        validator = Draft202012Validator(schemas["session.schema.json"], format_checker=FormatChecker())
        for path in sorted((ROOT / "examples").glob("*/session.json")):
            for err in validator.iter_errors(load(path)):
                p = "/".join(map(str, err.absolute_path))
                errors.append(f"{path.relative_to(ROOT)}:{p}: {err.message}")

    if errors:
        raise SystemExit("\n".join(errors))

    print("Repository validation: OK")


if __name__ == "__main__":
    main()

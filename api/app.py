from __future__ import annotations

import json
from pathlib import Path
from fastapi import FastAPI, HTTPException
from jsonschema import Draft202012Validator

from api.engine import translate

ROOT = Path(__file__).resolve().parents[1]
CANON = ROOT / "canon"
SCHEMA = json.loads((ROOT / "schemas" / "session.schema.json").read_text(encoding="utf-8"))
VALIDATOR = Draft202012Validator(SCHEMA)

app = FastAPI(
    title="Kairophonographe Reference API",
    version="0.6.0",
    description="Inspectable reference API for situated environmental-to-music mappings."
)

@app.get("/health")
def health():
    return {"status": "ok", "version": "0.6.0"}

@app.get("/v1/manifest")
def manifest():
    return json.loads((CANON / "manifest.json").read_text(encoding="utf-8"))

@app.get("/v1/mappings/{name}")
def mapping(name: str):
    allowed = {p.stem for p in CANON.glob("*_mapping.json")} | {"anti_recycling", "manifest"}
    if name not in allowed:
        raise HTTPException(status_code=404, detail="Unknown mapping")
    filename = f"{name}.json" if name in {"anti_recycling", "manifest"} else f"{name}.json"
    path = CANON / filename
    if not path.exists():
        path = CANON / f"{name}_mapping.json"
    return json.loads(path.read_text(encoding="utf-8"))

@app.post("/v1/translate")
def translate_session(session: dict):
    errors = sorted(VALIDATOR.iter_errors(session), key=lambda e: list(e.absolute_path))
    if errors:
        details = [{"path": "/".join(map(str, e.absolute_path)), "message": e.message} for e in errors[:20]]
        raise HTTPException(status_code=422, detail=details)
    return translate(session)

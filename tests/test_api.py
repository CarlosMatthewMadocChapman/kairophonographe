from fastapi.testclient import TestClient
from api.app import app
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["version"] == "0.6.0"


def test_manifest():
    r = client.get("/v1/manifest")
    assert r.status_code == 200
    assert r.json()["project"] == "Kairophonographe"


def test_translate():
    session = json.loads((ROOT / "examples/new-terrain/session.json").read_text(encoding="utf-8"))
    r = client.post("/v1/translate", json=session)
    assert r.status_code == 200
    assert "music_spec" in r.json()

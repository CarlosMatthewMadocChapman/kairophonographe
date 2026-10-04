from __future__ import annotations
import json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from api.engine import translate

if len(sys.argv) != 2:
    raise SystemExit("Usage: python scripts/render_example.py examples/<name>/session.json")
path = Path(sys.argv[1])
session = json.loads(path.read_text(encoding="utf-8"))
print(json.dumps(translate(session), ensure_ascii=False, indent=2))

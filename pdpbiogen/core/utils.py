import json
from pathlib import Path

def load_json(path):
    p = Path(path)
    with p.open("r", encoding="utf-8") as fh:
        return json.load(fh)

def save_json(path, obj):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8") as fh:



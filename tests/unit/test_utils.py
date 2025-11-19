import tempfile
from pathlib import Path
from pdpbiogen.core.utils import save_json, load_json

def test_save_load_json(tmp_path):
    data = {"a": 1}
    p = tmp_path / "test.json"
    save_json(p, data)
    loaded = load_json(p)
    assert loaded == data

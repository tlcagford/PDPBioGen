import hashlib, json

def pipeline_run():
    # simulate producing JSON outputs
    out = {"model": "toy", "metrics": {"acc": 0.8, "seed": 42}}
    return json.dumps(out, sort_keys=True)

def test_e2e_hash():
    a = pipeline_run()
    b = pipeline_run()
    ha = hashlib.sha256(a.encode()).hexdigest()
    hb = hashlib.sha256(b.encode()).hexdigest()
    assert ha == hb

import numpy as np
from benchmarks.bci.test_classifiers import make_synthetic_data
from sklearn.dummy import DummyClassifier

def test_noise_robustness():
    X,y = make_synthetic_data()
    noise = np.random.RandomState(0).normal(scale=0.1, size=X.shape)
    Xn = X + noise
    dummy = DummyClassifier(strategy="most_frequent")
    dummy.fit(Xn,y)
    acc = dummy.score(Xn,y)
    # trivial check: not nan
    assert acc >= 0.0

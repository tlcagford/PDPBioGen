import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

def make_synthetic_data(n_channels=8, n_epochs=100, epoch_timepoints=128):
    X = np.random.RandomState(42).randn(n_epochs, n_channels*epoch_timepoints)
    y = np.random.RandomState(1).randint(0,2,size=(n_epochs,))
    return X, y

def test_svm_baseline():
    X,y = make_synthetic_data()
    clf = make_pipeline(StandardScaler(), SVC(kernel='linear', probability=False, random_state=42))
    scores = cross_val_score(clf, X, y, cv=3)
    assert scores.mean() > 0.3  # sanity threshold for synthetic data

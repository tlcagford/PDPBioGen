import numpy as np

def toy_agent_optim(x, steps=10, lr=0.1):
    x = float(x)
    hist = []
    for _ in range(steps):
        grad = 2*(x-0.5)
        x = x - lr*grad
        hist.append(x)
    return hist

def test_agent_convergence():
    hist = toy_agent_optim(0.0, steps=20, lr=0.05)
    assert abs(hist[-1] - 0.5) < 0.1

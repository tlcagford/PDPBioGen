import numpy as np

def controller(fused):
    stress = (
        0.4 * (1 / fused[0]) +
        0.3 * fused[2] +
        0.3 * fused[5]
    )
    return np.clip(stress, 0, 3)

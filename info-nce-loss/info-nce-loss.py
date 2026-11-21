import numpy as np

def info_nce_loss(Z1: list, Z2: list, temperature: float = 0.1) -> float:
    """
    Returns the loss as a float.
    """
    S = np.dot(Z1, np.transpose(Z2)) / temperature
    x = 0
    for i in range(len(Z1)):
        m = np.max(S[i])
        e = np.exp(S[i][i] - m)
        e1 = 0
        for j in range(len(Z1)):
            e1 += np.exp(S[i][j] - m)
        x += np.log(e / e1)
    return float(-x / len(Z1))
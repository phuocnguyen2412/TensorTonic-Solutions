import numpy as np

def linear_layer_forward(X, W, b):
    X = np.array(X, dtype=float)
    W = np.array(W, dtype=float)
    b = np.array(b, dtype=float)

    Y = X @ W + b  # KHÔNG transpose

    return Y.tolist()
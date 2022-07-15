import numpy as np


def cost_function(x):

    x = x["binary1D"][0]

    return x, float(np.sum(x, axis=1))

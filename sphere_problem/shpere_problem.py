import numpy as np


def cost_function(x):

    x = x["real1D"][0]

    return x, float(np.sum(np.square(x), axis=1))

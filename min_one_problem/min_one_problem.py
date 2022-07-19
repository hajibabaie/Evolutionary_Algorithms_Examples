import copy
import numpy as np


def cost_function(x):

    for type_of_variable in x.keys():
        if type_of_variable == "binary1D":
            x = x["binary1D"][0]
        elif type_of_variable == "real1D":
            x = x["real1D"][0]
            x = copy.deepcopy(x)
            x[:, x[0, :] >= 0.5] = 1
            x[:, x[0, :] < 0.5] = 0

    return x, float(np.sum(x, axis=1))

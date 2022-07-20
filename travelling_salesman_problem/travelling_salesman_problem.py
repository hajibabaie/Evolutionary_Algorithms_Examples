from evolutionary_algorithms_examples.travelling_salesman_problem.data import Data
import numpy as np


class TSP:

    def __init__(self):

        self._model_data = Data.load()


    def cost_function(self, x):

        distances = self._model_data["distances"]

        if "permutation1D" in x.keys():

            x_parsed = x["permutation1D"][0]

        elif "real1D" in x.keys():

            x = x["real1D"][0]

            x_parsed = np.argsort(x, axis=1)

        objective_function = 0
        for i in range(int(x_parsed.shape[1]) - 1):

            objective_function += distances[x_parsed[0, i], x_parsed[0, i + 1]]

        objective_function += distances[x_parsed[0, -1], x_parsed[0, 0]]


        return x_parsed, objective_function

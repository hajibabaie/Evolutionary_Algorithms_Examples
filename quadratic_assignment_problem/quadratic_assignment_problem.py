from evolutionary_algorithms_examples.quadratic_assignment_problem.data import Data
import numpy as np
import copy


class QuadraticAssignmentProblem:

    def __init__(self):

        self._model_data = Data.load()

    def _parsed_solution(self, x):

        number_of_facilities = int(self._model_data["weights_between_facilities"].shape[0])
        return x[:, :number_of_facilities]


    def cost_function(self, x):

        weights = self._model_data["weights_between_facilities"]

        distances = self._model_data["distances"]

        if "permutation1D" in x.keys():

            x = x["permutation1D"][0]

        elif "real1D" in x.keys():

            x = x["real1D"][0]
            x = copy.deepcopy(x)
            x = np.argsort(x, axis=1)


        x_parsed = self._parsed_solution(x)

        cost_function = 0
        for i in range(int(x_parsed.shape[1]) - 1):

            cost_function += distances[x_parsed[0, i], x_parsed[0, i + 1]] * (weights[i, i + 1] + weights[i + 1, i])

        solution_parsed = {
            "x_parsed": x_parsed,
        }
        return solution_parsed, cost_function

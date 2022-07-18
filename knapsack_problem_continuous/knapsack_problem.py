from evolutionary_algorithms_examples.knapsack_problem_continuous.data import Data
import numpy as np
import copy


class KnapsackProblemContinuous:

    def __init__(self):

        self._model_data = Data.load()

    def cost_function(self, x):

        x = x["real1D"][0]

        values = self._model_data["values_of_items"].reshape(x.shape)
        weights = self._model_data["weights_of_items"].reshape(x.shape)
        knapsack_capacity = self._model_data["knapsack_capacity"]

        x_parsed = copy.deepcopy(x)

        values_gained = np.dot(x_parsed, values.T)[0, 0]
        values_not_gained = np.dot(1 - x_parsed, values.T)[0, 0]

        weights_gained = np.dot(x_parsed, weights.T)[0, 0]
        weights_not_gained = np.dot(1 - x_parsed, weights.T)[0, 0]

        objective_function = values_not_gained

        knapsack_capacity_violation = np.maximum((weights_gained / knapsack_capacity - 1), 0)

        cost = objective_function * (1 + 10 * knapsack_capacity_violation)

        solution_parsed = {
            "values_gained": values_gained,
            "values_not_gained": values_not_gained,
            "weights_gained": weights_gained,
            "weights_not_gained": weights_not_gained,
            "knapsack_capacity_violation": knapsack_capacity_violation
        }

        return solution_parsed, cost

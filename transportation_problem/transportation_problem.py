from evolutionary_algorithms_examples.transportation_problem.data import Data
import numpy as np


class TransportationProblem:


    def __init__(self):

        self._model_data = Data.load()


    def _parsed_solution(self, x):

        customers_demand = self._model_data["customers_demand"]

        x = x["real2D"][0]
        x_normalized = np.divide(x, np.sum(x, axis=0, keepdims=True))
        x_parsed = np.multiply(x_normalized, customers_demand)

        return x_parsed

    def cost_function(self, x):

        suppliers_capacity = self._model_data["suppliers_capacity"]
        distances = self._model_data["distances"]
        x_parsed = self._parsed_solution(x)
        supplier_sent = np.sum(x_parsed, axis=1, keepdims=True).T
        supplier_capacity_violations = np.maximum(np.divide(supplier_sent, suppliers_capacity) - 1, 0)
        supplier_capacity_violations_average = np.average(supplier_capacity_violations)
        objective_function = np.sum(np.multiply(x_parsed, distances))
        cost_function = objective_function * (1 + 10 * supplier_capacity_violations_average)

        solution_parsed = {
            "x_parsed": x_parsed,
            "suppliers_capacity_violation": supplier_capacity_violations,
            "suppliers_capacity_violations_average": supplier_capacity_violations_average,
            "objective_function": objective_function,
        }

        return solution_parsed, cost_function

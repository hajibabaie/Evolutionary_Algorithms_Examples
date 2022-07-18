from evolutionary_algorithms_examples.transportation_problem_with_fixed_costs.data import Data
import numpy as np



class TransportationProblemWithFixedCost:

    def __init__(self):

        self._model_data = Data.load()

    def _parse_solution(self, real, binary):

        customers_demand = self._model_data["customers_demand"]

        x_real_binary = np.multiply(real, binary.T)
        x_real_binary_sum = np.sum(x_real_binary, axis=0, keepdims=True)
        x_real_binary_normalized = np.divide(x_real_binary, x_real_binary_sum)
        x_parsed = np.multiply(x_real_binary_normalized, customers_demand)

        return x_parsed

    def cost_function(self, x):

        suppliers_capacity = self._model_data["suppliers_capacity"]
        suppliers_fixed_cost = self._model_data["suppliers_fixed_cost"]
        distances = self._model_data["distances"]

        x_real = x["real2D"][0]
        x_binary = x["binary1D"][0]

        x_parsed = self._parse_solution(x_real, x_binary)

        objective_function_real_part = np.sum(np.multiply(x_parsed, distances))
        objective_function_binary_part = np.dot(x_binary, suppliers_fixed_cost.T)[0, 0]
        objective_function = objective_function_real_part + objective_function_binary_part

        suppliers_sent = np.sum(x_parsed, axis=1, keepdims=True)
        supplier_capacity_violations = np.maximum(np.divide(suppliers_sent.T, suppliers_capacity) - 1, 0)
        supplier_capacity_violations_average = np.average(supplier_capacity_violations)

        cost_function = objective_function * (1 + 10 * supplier_capacity_violations_average)

        solution_parsed = {
            "x_parsed": x_parsed,
            "objective_function_real_part": objective_function_real_part,
            "objective_function_binary_part": objective_function_binary_part,
            "objective_function": objective_function,
            "supplier_sent": suppliers_sent,
            "supplier_capacity_violations": supplier_capacity_violations,
            "supplier_capacity_violations_average": supplier_capacity_violations_average
        }

        return solution_parsed, cost_function

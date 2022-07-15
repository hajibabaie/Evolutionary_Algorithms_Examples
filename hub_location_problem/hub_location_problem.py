from evolutionary_algorithms_examples.hub_location_problem.data import Data
import numpy as np



class HubLocationProblem:

    def __init__(self):

        self._model_data = Data.load()


    def cost_function(self, x):

        x = x["binary1D"][0]

        x_inf = np.copy(x)

        x_inf[x_inf == 0] = 1e5

        distances = self._model_data["distances"]

        number_of_customers = len(self._model_data["customers_x"])

        customers_demand = np.reshape(self._model_data["customers_demand"], (1, number_of_customers))

        servers_cost = np.reshape(self._model_data["servers_cost"], (1, distances.shape[1]))

        distances_in_x = np.multiply(x_inf, distances)

        solution = np.zeros((number_of_customers, 2))

        solution[:, 0:1] = np.min(distances_in_x, axis=1, keepdims=True)
        solution[:, 1:2] = np.argmin(distances_in_x, axis=1, keepdims=True)

        opened_hubs = list(set([int(i) for i in solution[:, 1:2]]))

        objective_function_first_part = np.dot(customers_demand, solution[:, 0:1])[0, 0]
        objective_function_second_part = 100 * np.sum(servers_cost[0, opened_hubs])

        cost = float(objective_function_first_part + objective_function_second_part)
        #
        # if np.all(x[0, :] == 0):
        #     cost = 1e30

        return solution, cost


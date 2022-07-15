import numpy as np
import os


class Data:


    def __init__(self,
                 number_of_customers,
                 number_of_servers,
                 customers_demand_min,
                 customers_demand_max,
                 servers_fixed_cost_min,
                 servers_fixed_cost_max):

        self._number_of_customers = number_of_customers
        self._number_of_servers = number_of_servers
        self._customer_demand_min = customers_demand_min
        self._customer_demand_max = customers_demand_max
        self._servers_fixed_cost_min = servers_fixed_cost_min
        self._servers_fixed_cost_max = servers_fixed_cost_max


    def create_and_save(self):

        os.makedirs("./data", exist_ok=True)

        customers_x = np.random.randint(0, 100, self._number_of_customers)
        customers_y = np.random.randint(0, 100, self._number_of_customers)
        customers_demand = np.random.uniform(self._customer_demand_min,
                                             self._servers_fixed_cost_max,
                                             self._number_of_customers)

        servers_x = np.random.randint(0, 100, self._number_of_servers)
        servers_y = np.random.randint(0, 100, self._number_of_servers)
        servers_cost = np.random.uniform(self._servers_fixed_cost_min,
                                         self._servers_fixed_cost_max,
                                         self._number_of_servers)

        distances = np.zeros((self._number_of_customers, self._number_of_servers))

        for i in range(self._number_of_customers):
            for j in range(self._number_of_servers):
                distances[i, j] = np.sqrt(np.square(customers_x[i] - servers_x[j]) +
                                          np.square(customers_y[i] - servers_y[j]))

        np.save("./data/customers_x.npy", customers_x)
        np.save("./data/customers_y.npy", customers_y)
        np.save("./data/customers_demand.npy", customers_demand)

        np.save("./data/servers_x.npy", servers_x)
        np.save("./data/servers_y.npy", servers_y)
        np.save("./data/servers_cost.npy", servers_cost)

        np.save("./data/distances.npy", distances)

    @staticmethod
    def load():

        out = {
            "customers_x": np.load("./data/customers_x.npy"),
            "customers_y": np.load("./data/customers_y.npy"),
            "customers_demand": np.load("./data/customers_demand.npy"),
            "servers_x": np.load("./data/servers_x.npy"),
            "servers_y": np.load("./data/servers_y.npy"),
            "servers_cost": np.load("./data/servers_cost.npy"),
            "distances": np.load("./data/distances.npy"),
        }

        return out

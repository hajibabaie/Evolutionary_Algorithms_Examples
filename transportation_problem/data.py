import os

import numpy as np


class Data:

    def __init__(self,
                 number_of_suppliers,
                 number_of_customers,
                 customers_demand_min,
                 customers_demand_max):

        self._number_of_suppliers = number_of_suppliers
        self._number_of_customers = number_of_customers
        self._customers_demand_min = customers_demand_min
        self._customers_demand_max = customers_demand_max


    def create_and_save(self):

        suppliers_x = np.random.randint(0, 100, self._number_of_suppliers)
        suppliers_y = np.random.randint(0, 100, self._number_of_suppliers)

        customers_x = np.random.randint(0, 100, self._number_of_customers)
        customers_y = np.random.randint(0, 100, self._number_of_customers)

        distances = np.zeros((self._number_of_suppliers, self._number_of_customers))
        for i in range(self._number_of_suppliers):
            for j in range(self._number_of_customers):
                distances[i, j] = np.sqrt(np.square(suppliers_x[i] - customers_x[j]) +
                                          np.square(suppliers_y[i] - customers_y[j]))

        customers_demand = np.random.uniform(self._customers_demand_min,
                                             self._customers_demand_max,
                                             (1, self._number_of_customers))

        a = float(np.sum(customers_demand) / self._number_of_suppliers)

        supplier_capacity = np.random.uniform(a, 1.2 * a, (1, self._number_of_suppliers))


        os.makedirs("./data", exist_ok=True)

        np.save("./data/distances.npy", distances)
        np.save("./data/customers_demand.npy", customers_demand)
        np.save("./data/suppliers_capacity.npy", supplier_capacity)

    @staticmethod
    def load():

        out = {
            "distances": np.load("./data/distances.npy"),
            "customers_demand": np.load("./data/customers_demand.npy"),
            "suppliers_capacity": np.load("./data/suppliers_capacity.npy")
        }

        return out

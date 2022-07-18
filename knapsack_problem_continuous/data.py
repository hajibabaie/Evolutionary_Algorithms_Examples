import numpy as np
import os


class Data:

    def __init__(self,
                 number_of_items=100):

        self._number_of_items = number_of_items
        self._min_values = 10
        self._max_values = 90
        self._min_weights = 100,
        self._max_weights = 500
        self._knapsack_capacity = None

    def create_and_save(self):

        values_of_items = np.random.uniform(self._min_values, self._max_values, self._number_of_items)

        weights_of_items = np.random.uniform(self._min_weights, self._max_weights, self._number_of_items)

        self._knapsack_capacity = int(np.sum(weights_of_items) / 2)

        os.makedirs("./data", exist_ok=True)
        np.save("./data/values.npy", values_of_items)
        np.save("./data/weights.npy", weights_of_items)

    @staticmethod
    def load():

        out = {
            "values_of_items": np.load("./data/values.npy"),
            "weights_of_items": np.load("./data/weights.npy"),
            "knapsack_capacity": int(np.sum(np.load("./data/weights.npy")) / 8)
        }

        return out

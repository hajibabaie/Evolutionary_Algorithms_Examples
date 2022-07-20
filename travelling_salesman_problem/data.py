import numpy as np
import os


class Data:

    def __init__(self, number_of_nodes):

        self._number_of_nodes = number_of_nodes


    def create_and_save(self):

        os.makedirs("./data", exist_ok=True)

        locations_x = np.random.randint(0, 100, self._number_of_nodes)
        locations_y = np.random.randint(0, 100, self._number_of_nodes)

        distance_between_locations = np.zeros((self._number_of_nodes, self._number_of_nodes))
        for i in range(self._number_of_nodes):
            for j in range(i + 1, self._number_of_nodes):
                distance_between_locations[i, j] = np.sqrt(np.square(locations_x[i] - locations_x[j]) +
                                                           np.square(locations_y[i] - locations_y[j]))

                distance_between_locations[j, i] = distance_between_locations[i, j]

        np.save("./data/locations_x.npy", locations_x)
        np.save("./data/locations_y.npy", locations_y)
        np.save("./data/distances.npy", distance_between_locations)


    @staticmethod
    def load():

        out = {
            "locations_x": np.load("./data/locations_x.npy"),
            "locations_y": np.load("./data/locations_y.npy"),
            "distances": np.load("./data/distances.npy")
        }

        return out

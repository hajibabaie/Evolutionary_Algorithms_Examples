import os
import numpy as np


class Data:

    def __init__(self,
                 number_of_facilities,
                 number_of_locations):

        self._number_of_facilities = number_of_facilities
        self._number_of_locations = number_of_locations

    def create_and_save(self):

        locations_x = np.random.uniform(0, 100, self._number_of_locations)
        locations_y = np.random.uniform(0, 100, self._number_of_locations)

        weights_between_facilities = np.random.uniform(10, 20, (self._number_of_facilities, self._number_of_facilities))
        weights_between_facilities -= np.diag(np.diag(weights_between_facilities))

        distances = np.zeros((self._number_of_locations, self._number_of_locations))
        for i in range(self._number_of_locations):
            for j in range(i + 1, self._number_of_locations):
                distances[i, j] = np.sqrt(np.square(locations_x[i] - locations_x[j]) +
                                          np.square(locations_y[i] - locations_y[j]))

                distances[j, i] = distances[i, j]

        os.makedirs("./data", exist_ok=True)
        np.save("./data/locations_x.npy", locations_x)
        np.save("./data/locations_y.npy", locations_y)
        np.save("./data/distances.npy", distances)
        np.save("./data/weights_between_facilities.npy", weights_between_facilities)

    @staticmethod
    def load():

        out = {
            "locations_x": np.load("./data/locations_x.npy"),
            "locations_y": np.load("./data/locations_y.npy"),
            "distances": np.load("./data/distances.npy"),
            "weights_between_facilities": np.load("./data/weights_between_facilities.npy")
        }

        return out

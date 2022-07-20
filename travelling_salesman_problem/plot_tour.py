import os
import numpy as np
import matplotlib.pyplot as plt



def tour(solution, model_data, solution_method):

    salesman_tour = solution.solution_parsed
    locations_x = model_data["locations_x"]
    locations_y = model_data["locations_y"]

    os.makedirs("./figures", exist_ok=True)
    plt.figure(dpi=300, figsize=(10, 6))
    plt.scatter(locations_x, locations_y, marker="o", s=16, c="red", label="nodes")
    for i in range(len(locations_x) - 1):

        plt.text(locations_x[salesman_tour[0, i]], locations_y[salesman_tour[0, i]], str(salesman_tour[0, i]))

        if i == 0:

            plt.plot([locations_x[salesman_tour[0, i]], locations_x[salesman_tour[0, i + 1]]],
                     [locations_y[salesman_tour[0, i]], locations_y[salesman_tour[0, i + 1]]], color="green")

        else:

            plt.plot([locations_x[salesman_tour[0, i]], locations_x[salesman_tour[0, i + 1]]],
                     [locations_y[salesman_tour[0, i]], locations_y[salesman_tour[0, i + 1]]], color="black")


    plt.plot([locations_x[salesman_tour[0, -1]], locations_x[salesman_tour[0, 0]]],
             [locations_y[salesman_tour[0, -1]], locations_y[salesman_tour[0, 0]]], color="red")

    plt.savefig(f"./figures/tour_{solution_method}.png")

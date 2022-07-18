import matplotlib.pyplot as plt
import os


def plot(solution, model_data):


    solution = solution.solution_parsed["x_parsed"]
    location_x = model_data["locations_x"]
    location_y = model_data["locations_y"]

    os.makedirs("./figures", exist_ok=True)
    plt.figure(dpi=300, figsize=(10, 6))
    plt.scatter(location_x, location_y, marker="o", s=16, c="red", label="potential locations")
    for i in range(int(solution.shape[1])):
        plt.scatter(location_x[solution[0, i]],
                    location_y[solution[0, i]], marker="o", s=16, c="green")
        plt.text(location_x[solution[0, i]],
                 location_y[solution[0, i]], str(i))
    plt.legend()
    plt.savefig("./figures/assignment.png")

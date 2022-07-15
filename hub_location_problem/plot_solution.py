import matplotlib.pyplot as plt
import numpy as np
import os


def plot_assignment(solution, model_data):


    os.makedirs("./figures", exist_ok=True)

    plt.figure(dpi=300, figsize=(10, 6))

    customers_x = model_data["customers_x"]
    customers_y = model_data["customers_y"]

    servers_x = model_data["servers_x"]
    servers_y = model_data["servers_y"]

    opened_servers = solution.position["binary1D"][0]

    opened_servers_x = servers_x[np.argwhere(opened_servers[0, :] != 0)].ravel()
    opened_servers_y = servers_y[np.argwhere(opened_servers[0, :] != 0)].ravel()

    plt.scatter(customers_x, customers_y, marker="o", c="blue", s=8, label="customers")
    plt.scatter(servers_x, servers_y, marker="x", c="red", s=8, label="potential servers")
    plt.scatter(opened_servers_x, opened_servers_y, marker="x", c="green", s=26, label="opened servers")

    active_servers = solution.solution_parsed[:, 1]

    for i in range(len(customers_x)):

        plt.plot([customers_x[i], servers_x[int(active_servers[i])]],
                 [customers_y[i], servers_y[int(active_servers[i])]], "--", color="black")

    plt.legend()

    plt.savefig("./figures/customers_servers.png")




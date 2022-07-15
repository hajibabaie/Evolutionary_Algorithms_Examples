from evolutionary_algorithms_examples.hub_location_problem.data import Data
from evolutionary_algorithms.genetic_algorithm import GA
from evolutionary_algorithms_examples.hub_location_problem.hub_location_problem import HubLocationProblem
from evolutionary_algorithms_examples.hub_location_problem.plot_solution import plot_assignment


def main():

    # data = Data(number_of_customers=200,
    #             number_of_servers=50,
    #             customers_demand_min=5,
    #             customers_demand_max=50,
    #             servers_fixed_cost_min=500,
    #             servers_fixed_cost_max=1000)
    #
    # data.create_and_save()

    model_data = Data.load()

    type_number_of_variables = {"binary1D": [len(model_data["servers_x"])]}

    problem = HubLocationProblem()
    cost_func = problem.cost_function

    solution_method = GA(cost_function=cost_func,
                         type_number_of_variables=type_number_of_variables,
                         max_iteration=100,
                         number_of_population=50,
                         parents_selection_method="roulette_wheel_selection",
                         selection_pressure_for_roulette_wheel=7,
                         crossover_method="uniform",
                         crossover_percentage=0.8,
                         mutation_percentage=0.3,
                         mutation_rate=0.02,
                         plot_cost_function=True)

    solution_best, run_time = solution_method.run()
    plot_assignment(solution_best, model_data)

    return solution_best, run_time


if __name__ == "__main__":

    solution, runtime = main()
from evolutionary_algorithms_examples.sphere_problem.shpere_problem import cost_function
from evolutionary_algorithms.genetic_algorithm import GA


def main():


    cost_func = cost_function

    type_number_of_variables = {"real1D": [10]}

    solution_method = GA(cost_function=cost_func,
                         type_number_of_variables=type_number_of_variables,
                         min_range_of_real_variables=-10,
                         max_range_of_real_variables=10,
                         max_iteration=200,
                         number_of_population=40,
                         parents_selection_method="roulette_wheel_selection",
                         selection_pressure_for_roulette_wheel=7,
                         tournament_size=5,
                         crossover_percentage=0.7,
                         mutation_percentage=0.4,
                         mutation_rate=0.03,
                         gamma_for_crossover=0.1,
                         gamma_for_mutation=0.1,
                         plot_cost_function=True,
                         y_axis="log")

    solution_best, run_time = solution_method.run()

    return solution_best, run_time


if __name__ == "__main__":

    solution, runtime = main()

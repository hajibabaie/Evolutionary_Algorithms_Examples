from evolutionary_algorithms_examples.sphere_problem.shpere_problem import cost_function
from evolutionary_algorithms.genetic_algorithm import GA
from evolutionary_algorithms.particle_swarm_optimization import PSO


def main():


    cost_func = cost_function

    type_number_of_variables = {"real1D": [10]}

    # solution_method = GA(cost_function=cost_func,
    #                      type_number_of_variables=type_number_of_variables,
    #                      min_range_of_real_variables=-10,
    #                      max_range_of_real_variables=10,
    #                      max_iteration=200,
    #                      number_of_population=40,
    #                      parents_selection_method="roulette_wheel_selection",
    #                      selection_pressure_for_roulette_wheel=7,
    #                      tournament_size=5,
    #                      crossover_percentage=0.7,
    #                      mutation_percentage=0.4,
    #                      mutation_rate=0.03,
    #                      gamma_for_crossover=0.1,
    #                      gamma_for_mutation=0.1,
    #                      plot_cost_function=True,
    #                      y_axis="log")

    # solution_best, run_time = solution_method.run()
    #
    # return solution_best, run_time

    solution_method = PSO(cost_function=cost_func,
                          type_number_of_variables=type_number_of_variables,
                          min_range_of_variables=-10,
                          max_range_of_variables=10,
                          max_iteration=7500,
                          number_of_particles=20,
                          inertia_rate=0.7298,
                          inertia_damping_rate=1,
                          personal_learning_rate=1.4962,
                          global_learning_rate=1.4962,
                          tempo_limit=True,
                          mirroring_effect=False,
                          plot_cost_function=True,
                          y_axis="log")

    populations, solution_best, run_time = solution_method.run()

    return populations, solution_best, run_time


if __name__ == "__main__":

    pops, solution, runtime = main()

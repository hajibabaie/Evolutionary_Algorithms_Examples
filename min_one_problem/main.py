from evolutionary_algorithms_examples.min_one_problem.min_one_problem import cost_function
from evolutionary_algorithms.genetic_algorithm import GA
from evolutionary_algorithms.particle_swarm_optimization import PSO


def main():


    cost_func = cost_function

    # type_number_of_variables = {"binary1D": [600]}

    type_number_of_variables = {"real1D": [600]}

    # solution_method = GA(cost_function=cost_func,
    #                      type_number_of_variables=type_number_of_variables,
    #                      max_iteration=100,
    #                      number_of_population=150,
    #                      parents_selection_method="roulette_wheel_selection",
    #                      selection_pressure_for_roulette_wheel=7,
    #                      tournament_size=2,
    #                      crossover_method="uniform",
    #                      crossover_percentage=0.9,
    #                      mutation_percentage=0.4,
    #                      mutation_rate=0.03,
    #                      gamma_for_crossover=0.1,
    #                      gamma_for_mutation=0.1,
    #                      plot_cost_function=True)
    #
    # solution_best, run_time = solution_method.run()
    #
    # return solution_best, run_time

    solution_method = PSO(cost_function=cost_func,
                          type_number_of_variables=type_number_of_variables,
                          min_range_of_variables=0,
                          max_range_of_variables=1,
                          max_iteration=8,
                          number_of_particles=150,
                          inertia_rate=0.7298,
                          inertia_damping_rate=1,
                          personal_learning_rate=1.5,
                          global_learning_rate=1.5,
                          tempo_limit=True,
                          mutation_for_real=True,
                          gamma_for_real_mutation=0.3,
                          plot_cost_function=True)

    solution_best, run_time = solution_method.run()

    return solution_best, run_time


if __name__ == "__main__":

    solution, runtime = main()

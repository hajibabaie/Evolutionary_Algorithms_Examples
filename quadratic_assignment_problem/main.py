from evolutionary_algorithms_examples.quadratic_assignment_problem.data import Data
from evolutionary_algorithms_examples.quadratic_assignment_problem.quadratic_assignment_problem import QuadraticAssignmentProblem
from evolutionary_algorithms_examples.quadratic_assignment_problem.plot_assignment import plot
from evolutionary_algorithms.genetic_algorithm import GA
from evolutionary_algorithms.particle_swarm_optimization import PSO


def main():
    #
    # data = Data(number_of_facilities=10,
    #             number_of_locations=20)
    #
    # data.create_and_save()

    model_data = Data.load()
    # type_number_of_variables = {"permutation1D": [len(model_data["locations_x"])]}

    type_number_of_variables = {"real1D": [len(model_data["locations_x"])]}

    problem = QuadraticAssignmentProblem()
    cost_func = problem.cost_function

    # solution_method = GA(cost_function=cost_func,
    #                      type_number_of_variables=type_number_of_variables,
    #                      max_iteration=200,
    #                      number_of_population=20,
    #                      parents_selection_method="roulette_wheel_selection",
    #                      selection_pressure_for_roulette_wheel=7,
    #                      crossover_percentage=0.7,
    #                      mutation_percentage=0.4,
    #                      mutation_rate=0.02,
    #                      gamma_for_crossover=0.3,
    #                      gamma_for_mutation=0.3,
    #                      plot_cost_function=True)
    #
    # solution_best, run_time = solution_method.run()
    #
    # plot(solution_best, model_data, "ga")

    # return solution_best, run_time

    solution_method = PSO(cost_function=cost_func,
                          type_number_of_variables=type_number_of_variables,
                          min_range_of_variables=0,
                          max_range_of_variables=1,
                          max_iteration=200,
                          number_of_particles=100,
                          inertia_rate=1,
                          inertia_damping_rate=0.99,
                          personal_learning_rate=1.6,
                          global_learning_rate=1.6,
                          tempo_limit=True,
                          plot_cost_function=True,
                          mutation_for_real=True,
                          mutation_for_permutation=True)

    solution_best, run_time = solution_method.run()

    plot(solution_best, model_data, "pso")

    return solution_best, run_time


if __name__ == "__main__":

    solution, runtime = main()
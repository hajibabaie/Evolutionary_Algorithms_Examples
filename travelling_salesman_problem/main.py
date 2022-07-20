from evolutionary_algorithms_examples.travelling_salesman_problem.data import Data
from evolutionary_algorithms_examples.travelling_salesman_problem.travelling_salesman_problem import TSP
from evolutionary_algorithms_examples.travelling_salesman_problem.plot_tour import tour
from evolutionary_algorithms.genetic_algorithm import GA
from evolutionary_algorithms.particle_swarm_optimization import PSO


def main():

    # data = Data(number_of_nodes=100)
    # data.create_and_save()
    model_data = Data.load()

    problem = TSP()
    cost_func = problem.cost_function

    type_number_of_variables_ga = {"permutation1D": [len(model_data["locations_x"])]}
    solution_method = GA(cost_function=cost_func,
                         type_number_of_variables=type_number_of_variables_ga,
                         max_iteration=2500,
                         number_of_population=100,
                         parents_selection_method="roulette_wheel_selection",
                         selection_pressure_for_roulette_wheel=7,
                         crossover_percentage=0.8,
                         mutation_percentage=0.4,
                         mutation_rate=0.02,
                         plot_cost_function=True)

    solution_best, run_time = solution_method.run()
    tour(solution_best, model_data, "ga")


    return solution_best, run_time

    # type_number_of_variables_pso = {"real1D": [len(model_data["locations_x"])]}
    # solution_method = PSO(cost_function=cost_func,
    #                       type_number_of_variables=type_number_of_variables_pso,
    #                       min_range_of_variables=0,
    #                       max_range_of_variables=1,
    #                       max_iteration=500,
    #                       number_of_particles=200,
    #                       inertia_rate=0.7298,
    #                       inertia_damping_rate=1,
    #                       personal_learning_rate=1.4962,
    #                       global_learning_rate=1.4962,
    #                       tempo_limit=True,
    #                       plot_cost_function=True,
    #                       mutation_for_real=True,
    #                       mutation_for_permutation=True)
    #
    # solution_best, run_time = solution_method.run()
    # tour(solution_best, model_data, "pso")
    #
    # return solution_best, run_time


if __name__ == "__main__":

    solution, runtime = main()

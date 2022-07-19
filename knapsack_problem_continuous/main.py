from evolutionary_algorithms_examples.knapsack_problem_continuous.data import Data
from evolutionary_algorithms_examples.knapsack_problem_continuous.knapsack_problem import KnapsackProblemContinuous
from evolutionary_algorithms.genetic_algorithm import GA
from evolutionary_algorithms.particle_swarm_optimization import PSO

def main():


    # data = Data(number_of_items=500)
    #
    # data.create_and_save()

    model_data = Data.load()

    type_number_of_variables = {"real1D": [len(model_data["values_of_items"])]}

    problem = KnapsackProblemContinuous()
    cost_func = problem.cost_function

    # solution_method = GA(cost_function=cost_func,
    #                      type_number_of_variables=type_number_of_variables,
    #                      min_range_of_real_variables=0,
    #                      max_range_of_real_variables=1,
    #                      max_iteration=500,
    #                      number_of_population=100,
    #                      parents_selection_method="roulette_wheel_selection",
    #                      selection_pressure_for_roulette_wheel=7,
    #                      crossover_percentage=0.8,
    #                      mutation_percentage=0.4,
    #                      mutation_rate=0.2,
    #                      gamma_for_crossover=0.3,
    #                      gamma_for_mutation=0.3,
    #                      plot_cost_function=True)
    #
    # best_solution, run_time = solution_method.run()
    #
    # return best_solution, run_time

    solution_method = PSO(cost_function=cost_func,
                          type_number_of_variables=type_number_of_variables,
                          min_range_of_variables=0,
                          max_range_of_variables=1,
                          max_iteration=10,
                          number_of_particles=200,
                          inertia_rate=0.7298,
                          inertia_damping_rate=1,
                          personal_learning_rate=1.4962,
                          global_learning_rate=1.4962,
                          tempo_limit=True,
                          plot_cost_function=True,
                          mutation_for_real=True)

    solution_best, run_time = solution_method.run()

    return solution_best, run_time


if __name__ == "__main__":


    solution, runtime = main()

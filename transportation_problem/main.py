from evolutionary_algorithms_examples.transportation_problem.data import Data
from evolutionary_algorithms_examples.transportation_problem.transportation_problem import TransportationProblem
from evolutionary_algorithms.genetic_algorithm import GA
from evolutionary_algorithms.particle_swarm_optimization import PSO


def main():


    # data = Data(number_of_suppliers=50,
    #             number_of_customers=400,
    #             customers_demand_min=100,
    #             customers_demand_max=200)
    #
    # data.create_and_save()
    model_data = Data.load()

    problem = TransportationProblem()
    cost_func = problem.cost_function

    type_number_of_variables = {"real2D": [model_data["distances"].shape]}

    # solution_method = GA(cost_function=cost_func,
    #                      type_number_of_variables=type_number_of_variables,
    #                      min_range_of_real_variables=0,
    #                      max_range_of_real_variables=1,
    #                      max_iteration=12000,
    #                      number_of_population=80,
    #                      parents_selection_method="roulette_wheel_selection",
    #                      selection_pressure_for_roulette_wheel=7,
    #                      crossover_percentage=0.8,
    #                      mutation_percentage=0.4,
    #                      mutation_rate=0.02,
    #                      gamma_for_crossover=0.3,
    #                      gamma_for_mutation=0.3,
    #                      plot_cost_function=True)
    #
    # solution_best, run_time = solution_method.run()
    #
    #
    # return solution_best, run_time

    solution_method = PSO(cost_function=cost_func,
                          type_number_of_variables=type_number_of_variables,
                          min_range_of_variables=0,
                          max_range_of_variables=1,
                          max_iteration=500,
                          number_of_particles=80,
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

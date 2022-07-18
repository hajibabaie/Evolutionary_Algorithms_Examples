from evolutionary_algorithms_examples.transportation_problem.data import Data
from evolutionary_algorithms_examples.transportation_problem.transportation_problem import TransportationProblem
from evolutionary_algorithms.genetic_algorithm import GA


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

    solution_method = GA(cost_function=cost_func,
                         type_number_of_variables=type_number_of_variables,
                         min_range_of_real_variables=0,
                         max_range_of_real_variables=1,
                         max_iteration=12000,
                         number_of_population=80,
                         parents_selection_method="roulette_wheel_selection",
                         selection_pressure_for_roulette_wheel=7,
                         crossover_percentage=0.8,
                         mutation_percentage=0.4,
                         mutation_rate=0.02,
                         gamma_for_crossover=0.3,
                         gamma_for_mutation=0.3,
                         plot_cost_function=True)

    solution_best, run_time = solution_method.run()


    return solution_best, run_time


if __name__ == "__main__":

    solution, runtime = main()

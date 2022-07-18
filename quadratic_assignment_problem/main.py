from evolutionary_algorithms_examples.quadratic_assignment_problem.data import Data
from evolutionary_algorithms_examples.quadratic_assignment_problem.quadratic_assignment_problem import QuadraticAssignmentProblem
from evolutionary_algorithms_examples.quadratic_assignment_problem.plot_assignment import plot
from evolutionary_algorithms.genetic_algorithm import GA


def main():
    #
    # data = Data(number_of_facilities=10,
    #             number_of_locations=20)
    #
    # data.create_and_save()

    model_data = Data.load()
    type_number_of_variables = {"permutation1D": [len(model_data["locations_x"])]}

    problem = QuadraticAssignmentProblem()
    cost_func = problem.cost_function

    solution_method = GA(cost_function=cost_func,
                         type_number_of_variables=type_number_of_variables,
                         max_iteration=200,
                         number_of_population=20,
                         parents_selection_method="roulette_wheel_selection",
                         selection_pressure_for_roulette_wheel=7,
                         crossover_percentage=0.7,
                         mutation_percentage=0.4,
                         mutation_rate=0.02,
                         gamma_for_crossover=0.3,
                         gamma_for_mutation=0.3,
                         plot_cost_function=True)

    solution_best, run_time = solution_method.run()

    plot(solution_best, model_data)

    return solution_best, run_time


if __name__ == "__main__":

    solution, runtime = main()
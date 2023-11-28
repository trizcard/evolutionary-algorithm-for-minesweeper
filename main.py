from evolutionary_algorithm import EvolutionaryAlgorithm
import config
import utils

def create_solver_file(best_solution):
    with open("minesweeper_solver.py", "w") as file:
        file.write("from minesweeper import Minesweeper\n\n")
        file.write("import config\n")
        file.write("def solve():\n")
        file.write("    game = Minesweeper(config.BOARD_SIZE, config.NUM_MINES)\n")
        file.write("    moves = " + str(best_solution.genome) + "\n")
        for move in best_solution.genome:
            file.write(f"    game.open_cell({move[0]}, {move[1]})\n")
            file.write("    game.render()\n")
        file.write("\nif __name__ == '__main__':\n")
        file.write("    solve()\n")


def main():
    # Inicializa e executa o algoritmo evolutivo com as configurações do config.py
    ea = EvolutionaryAlgorithm(
        config.POPULATION_SIZE, 
        config.GENOME_LENGTH, 
        config.BOARD_SIZE, 
        config.NUM_MINES
    )
    ea.run(
        config.NUM_GENERATIONS, 
        config.NUM_BEST, 
        config.MUTATION_RATE
    )

    # Exibe a melhor solução encontrada
    best_solution = ea.get_best_solution()
    utils.create_solver_file(best_solution)
    print("Melhor solução encontrada:")
    print(best_solution.genome)
    print(f"Aptidão: {best_solution.fitness}")



if __name__ == "__main__":
    main()

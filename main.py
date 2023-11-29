
#Import dos demais arquivos
from evolutionary_algorithm import EvolutionaryAlgorithm
import config
import utils


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


# Verifica se este é o script principal sendo executado
if __name__ == "__main__":
    main()

from population import Population
from minesweeper import Minesweeper

class EvolutionaryAlgorithm:
    def __init__(self, population_size, genome_length, board_size, num_mines):
        self.population = Population(population_size, genome_length, board_size)
        self.minesweeper = Minesweeper(board_size, num_mines)
        self.generation = 0

    def run(self, num_generations, num_best, mutation_rate):
        """ Executa o algoritmo evolutivo por um número específico de gerações. """
        while self.generation < num_generations:
            self.population.evaluate_fitness(self.minesweeper)
            self.population.generate_new_generation(num_best, mutation_rate)
            self.generation += 1
            print(f"Geração {self.generation}: Melhor aptidão = {self.population.individuals[0].fitness}")

    def get_best_solution(self):
        """ Retorna o melhor indivíduo da população atual. """
        return max(self.population.individuals, key=lambda ind: ind.fitness)

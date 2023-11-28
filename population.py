import random
from individual import Individual

class Population:
    def __init__(self, size, genome_length, board_size):
        self.individuals = [Individual(genome_length, board_size) for _ in range(size)]

    def evaluate_fitness(self, minesweeper):
        """ Avalia a aptidão de todos os indivíduos na população. """
        for individual in self.individuals:
            individual.calculate_fitness(minesweeper)

    def select_best(self, num_best):
        """ Seleciona os 'num_best' melhores indivíduos. """
        sorted_individuals = sorted(self.individuals, key=lambda ind: ind.fitness, reverse=True)
        return sorted_individuals[:num_best]

    def generate_new_generation(self, num_best, mutation_rate):
        """ Gera uma nova geração a partir dos melhores indivíduos. """
        best_individuals = self.select_best(num_best)
        new_generation = best_individuals[:1]  # Mantém o melhor indivíduo
        
        # Cria novos indivíduos por mutação dos melhores
        while len(new_generation) < len(self.individuals):
            parent = random.choice(best_individuals)
            child = Individual(len(parent.genome), parent.board_size)
            child.genome = parent.genome[:]
            child.mutate(mutation_rate)
            new_generation.append(child)
        
        self.individuals = new_generation

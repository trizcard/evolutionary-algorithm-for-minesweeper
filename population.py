#Import dos demais arquivos
import random
from individual import Individual

# Define a classe Population, que representa uma população no algoritmo evolutivo
class Population:
    # Método construtor da classe
    def __init__(self, size, genome_length, board_size):
        # Cria uma população de indivíduos com o tamanho especificado
        self.individuals = [Individual(genome_length, board_size) for _ in range(size)]

    # Método para avaliar a aptidão de todos os indivíduos na população
    def evaluate_fitness(self, minesweeper):
        for individual in self.individuals:
            # Calcula a aptidão de cada indivíduo
            individual.calculate_fitness(minesweeper)

    # Método para selecionar os melhores indivíduos
    def select_best(self, num_best):
         # Ordena os indivíduos por aptidão e retorna os melhores
        sorted_individuals = sorted(self.individuals, key=lambda ind: ind.fitness, reverse=True)
        return sorted_individuals[:num_best]

    # Método para gerar uma nova geração a partir dos melhores indivíduos
    def generate_new_generation(self, num_best, mutation_rate):
        best_individuals = self.select_best(num_best)
        new_generation = best_individuals[:1]  # Mantém o melhor indivíduo
        
        # Cria novos indivíduos por mutação dos melhores
        while len(new_generation) < len(self.individuals):
            # Escolhe um pai aleatoriamente entre os melhores
            parent = random.choice(best_individuals)
            # Cria um novo indivíduo (filho) e aplica mutação
            child = Individual(len(parent.genome), parent.board_size)
            child.genome = parent.genome[:]
            child.mutate(mutation_rate)
            # Adiciona o novo indivíduo à nova geração
            new_generation.append(child)
            
        # Atualiza a população com a nova geração
        self.individuals = new_generation

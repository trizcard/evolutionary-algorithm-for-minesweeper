#Import dos demais arquivos
from population import Population
from minesweeper import Minesweeper

class EvolutionaryAlgorithm:
    # Método construtor da classe
    def __init__(self, population_size, genome_length, board_size, num_mines):
        # Inicializa a população com o tamanho da população, comprimento do genoma e tamanho do tabuleiro
        self.population = Population(population_size, genome_length, board_size)
        # Inicializa o jogo Campo Minado com o tamanho do tabuleiro e número de minas
        self.minesweeper = Minesweeper(board_size, num_mines)
        # Inicializa o contador de gerações
        self.generation = 0

    # Método para executar o algoritmo evolutivo
    def run(self, num_generations, num_best, mutation_rate):
        # Loop para executar o algoritmo até atingir o número de gerações especificado
        while self.generation < num_generations:
            self.population.evaluate_fitness(self.minesweeper)   # Avalia a aptidão da população atual
            self.population.generate_new_generation(num_best, mutation_rate) # Gera uma nova geração a partir dos melhores indivíduos e taxa de mutação
            self.generation += 1  # Incrementa o contador de gerações
            print(f"{self.generation}, {self.population.individuals[0].fitness}") # Imprime a aptidão do melhor indivíduo da geração atual

    # Método para obter a melhor solução da população atual
    def get_best_solution(self):
        return max(self.population.individuals, key=lambda ind: ind.fitness) # Retorna o indivíduo com a maior aptidão

import random

class Individual:
    def __init__(self, genome_length, board_size):
        self.board_size = board_size
        self.genome = self.generate_random_genome(genome_length)
        self.fitness = 0

    def generate_random_genome(self, length):
        """ Gera um genoma aleatório. Cada gene representa uma jogada (x, y) no tabuleiro. """
        genome = []
        for _ in range(length):
            x = random.randint(0, self.board_size - 1)
            y = random.randint(0, self.board_size - 1)
            genome.append((x, y))
        return genome

    def calculate_fitness(self, minesweeper):
        """ Avalia a aptidão do indivíduo. """
        # Resetar o estado do jogo
        minesweeper.reset()
        for move in self.genome:
            x, y = move
            if not minesweeper.open_cell(x, y):
                break  # A célula aberta é uma mina
        self.fitness = minesweeper.score()  # Define a pontuação como a aptidão

    def mutate(self, mutation_rate):
        """ Aplica mutação ao genoma do indivíduo. """
        for i in range(len(self.genome)):
            if random.random() < mutation_rate:
                self.genome[i] = (random.randint(0, self.board_size - 1), random.randint(0, self.board_size - 1))

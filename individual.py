import random #geração de numeros aleatórios

#representa um indivíduo no algoritmo evolutivo
class Individual:
    # Método construtor da classe
    def __init__(self, genome_length, board_size):
        self.board_size = board_size # Armazena o tamanho do tabuleiro
        self.genome = self.generate_random_genome(genome_length) # Gera um genoma aleatório para o indivíduo
        self.fitness = 0 # Inicializa a aptidão do indivíduo

    # Método para gerar um genoma aleatório. Cada gene representa uma jogada (x, y) no tabuleiro. 
    def generate_random_genome(self, length):
        genome = []
        for _ in range(length):
            # Gera uma jogada aleatória no tabuleiro
            x = random.randint(0, self.board_size - 1)
            y = random.randint(0, self.board_size - 1)
            genome.append((x, y))
        return genome

    # Método para calcular a aptidão do indivíduo
    def calculate_fitness(self, minesweeper):
        # Resetar o estado do jogo
        minesweeper.reset()
        for move in self.genome:
            x, y = move
            # Abre a célula no jogo; se for uma mina, interrompe o loop
            if not minesweeper.open_cell(x, y):
                break  
        self.fitness = minesweeper.score()  # Define a pontuação como a aptidão

    # Método para aplicar mutação ao genoma do indivíduo
    def mutate(self, mutation_rate):
        for i in range(len(self.genome)):
            # Aplica mutação com base na taxa de mutação
            if random.random() < mutation_rate:
                # Gera uma nova jogada aleatória e substitui no genoma
                self.genome[i] = (random.randint(0, self.board_size - 1), random.randint(0, self.board_size - 1))

    
    #Realiza o crossover de um ponto com outro indivíduo.           
    def crossover(self, other):
        # Escolhe um ponto aleatório para o crossover
        crossover_point = random.randint(1, len(self.genome) - 1)
        # Combina a parte do genoma antes do ponto de crossover do primeiro pai com a parte do genoma após o ponto de crossover do segundo pai
        child_genome = self.genome[:crossover_point] + other.genome[crossover_point:]

        # Retorna um novo indivíduo criado a partir do genoma combinado
        child = Individual(len(child_genome), self.board_size)
        child.genome = child_genome
        return child
    

        

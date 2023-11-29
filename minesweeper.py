# Importa o módulo random para geração de números aleatórios e tkinter para interface gráfica
import random
import tkinter as tk

class Minesweeper:
    # Método construtor da classe
    def __init__(self, size, num_mines):
        self.size = size # Define o tamanho do tabuleiro
        self.num_mines = num_mines # Define o número de minas
        self.board = self.create_board() # Cria o tabuleiro
        self.place_mines() # Coloca as minas no tabuleiro
        self.opened = [[False for _ in range(size)] for _ in range(size)]  # Rastrear células abertas


    # Cria uma matriz size x size com zeros
    def create_board(self):
        return [[0 for _ in range(self.size)] for _ in range(self.size)]

    # Método para colocar minas no tabuleiro
    def place_mines(self):
        mines_placed = 0
        while mines_placed < self.num_mines:
            # Escolhe uma posição aleatória para a mina
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            # Se não houver mina nessa posição, coloca uma mina e atualiza os vizinhos
            if self.board[y][x] != 'M':
                self.board[y][x] = 'M'
                self.update_neighbors(x, y)
                mines_placed += 1

     # Método para atualizar os números nas células vizinhas às minas
    def update_neighbors(self, x, y):
        for i in range(-1, 2):
            for j in range(-1, 2):
                nx, ny = x + i, y + j
                # Se a célula vizinha está dentro do tabuleiro e não é uma mina, incrementa o número
                if 0 <= nx < self.size and 0 <= ny < self.size and self.board[ny][nx] != 'M':
                    self.board[ny][nx] += 1

    # Método para abrir uma célula
    def open_cell(self, x, y):
        # Se a célula é uma mina ou já foi aberta, retorna False
        if self.board[y][x] == 'M' or self.opened[y][x]:
            return False
        # Marca a célula como aberta e retorna True
        self.opened[y][x] = True
        return True

    # Método para verificar se o jogo foi resolvido
    def is_solved(self):
        # Verifica se todas as células não-mina foram abertas
        for row in self.board:
            for cell in row:
                if cell == 0:
                    return False
        return True
    
    # Método para reiniciar o jogo
    def reset(self):
        self.board = self.create_board() # Cria um novo tabuleiro
        self.place_mines() # Coloca as minas novamente

    # Método para calcular a pontuação
    def score(self):
        # Exemplo: contagem de células abertas que não são minas
        score = 0
        for row in self.board:
            for cell in row:
                if cell != 'M' and cell != 0:
                    score += 1
        return score

    # Método para renderizar o tabuleiro no console
    def render(self):
        for y in range(self.size):
            for x in range(self.size):
                # Exibe o estado atual de cada célula
                if self.opened[y][x]:
                    print(self.board[y][x], end=' ')
                else:
                    print('X', end=' ')  # X representa uma célula fechada
            print()
        print()

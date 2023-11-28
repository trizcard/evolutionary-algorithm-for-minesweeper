import random
import tkinter as tk

class Minesweeper:
    def __init__(self, size, num_mines):
        self.size = size
        self.num_mines = num_mines
        self.board = self.create_board()
        self.place_mines()
        self.opened = [[False for _ in range(size)] for _ in range(size)]  # Rastrear células abertas


    def create_board(self):
        return [[0 for _ in range(self.size)] for _ in range(self.size)]

    def place_mines(self):
        mines_placed = 0
        while mines_placed < self.num_mines:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            if self.board[y][x] != 'M':
                self.board[y][x] = 'M'
                self.update_neighbors(x, y)
                mines_placed += 1

    def update_neighbors(self, x, y):
        for i in range(-1, 2):
            for j in range(-1, 2):
                nx, ny = x + i, y + j
                if 0 <= nx < self.size and 0 <= ny < self.size and self.board[ny][nx] != 'M':
                    self.board[ny][nx] += 1

    def open_cell(self, x, y):
        if self.board[y][x] == 'M' or self.opened[y][x]:
            return False
        self.opened[y][x] = True
        return True

    def is_solved(self):
        for row in self.board:
            for cell in row:
                if cell == 0:
                    return False
        return True
    
    def reset(self):
        """ Reinicia o jogo para o estado inicial. """
        self.board = self.create_board()
        self.place_mines()

    def score(self):
        """ Calcula a pontuação baseada no estado atual do jogo. """
        # Exemplo: contagem de células abertas que não são minas
        score = 0
        for row in self.board:
            for cell in row:
                if cell != 'M' and cell != 0:
                    score += 1
        return score

    def render(self):
        for y in range(self.size):
            for x in range(self.size):
                if self.opened[y][x]:
                    print(self.board[y][x], end=' ')
                else:
                    print('X', end=' ')  # X representa uma célula fechada
            print()
        print()

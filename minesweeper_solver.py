from minesweeper import Minesweeper
import config
import tkinter as tk
from tkinter import messagebox

class MinesweeperGUI:
    def __init__(self, master, game, moves):
        self.master = master
        self.game = game
        self.moves = moves
        self.buttons = [[tk.Button(master, width=2, height=1) for _ in range(game.size)] for _ in range(game.size)]
        for y in range(game.size):
            for x in range(game.size):
                btn = self.buttons[y][x]
                btn.grid(row=y, column=x)
        self.next_move()

    def next_move(self):
        if not self.moves:
            messagebox.showinfo('Fim', 'Todos os movimentos foram realizados!')
            return
        move = self.moves.pop(0)
        success = self.game.open_cell(*move)
        self.update_buttons()
        self.master.after(500, self.next_move)

    def update_buttons(self):
        for y in range(self.game.size):
            for x in range(self.game.size):
                btn = self.buttons[y][x]
                if self.game.opened[y][x]:
                    btn.config(text=str(self.game.board[y][x]))

def solve():
    root = tk.Tk()
    game = Minesweeper(config.BOARD_SIZE, config.NUM_MINES)
    moves = [(7, 2), (3, 12), (5, 8), (6, 17), (9, 15), (6, 15), (2, 15), (0, 14), (18, 0), (13, 17), (12, 14), (14, 16), (0, 10), (12, 7), (6, 12), (7, 13), (3, 2), (10, 4), (11, 4), (4, 0), (4, 10), (14, 8), (16, 9), (11, 18), (10, 8), (10, 3), (16, 16), (10, 6), (4, 5), (9, 0), (10, 16), (3, 1), (12, 2), (14, 16), (19, 3), (15, 8), (16, 15), (2, 5), (1, 15), (5, 7), (4, 12), (6, 11), (11, 0), (3, 15), (15, 1), (0, 7), (18, 19), (19, 16), (6, 0), (7, 7)]
    gui = MinesweeperGUI(root, game, moves)
    root.mainloop()

if __name__ == '__main__':
    solve()

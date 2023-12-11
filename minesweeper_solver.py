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
    moves = [(14, 6), (13, 12), (2, 5), (16, 10), (18, 17), (3, 6), (5, 5), (5, 17), (6, 11), (9, 0), (16, 12), (1, 15), (11, 13), (14, 7), (15, 0), (19, 9), (12, 15), (18, 1), (14, 5), (18, 3), (17, 10), (14, 13), (18, 3), (11, 2), (17, 9), (16, 8), (0, 7), (10, 7), (4, 18), (15, 18), (12, 1), (15, 14), (2, 10), (10, 7), (10, 14), (17, 13), (5, 19), (17, 5), (18, 8), (16, 5), (16, 6), (19, 9), (2, 8), (16, 19), (10, 6), (8, 5), (17, 10), (11, 15), (2, 12), (3, 17)]
    gui = MinesweeperGUI(root, game, moves)
    root.mainloop()

if __name__ == '__main__':
    solve()

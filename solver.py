# Função para criar um arquivo de solução para o Campo Minado
def create_solver_file(best_solution):
     # Abre (ou cria) um arquivo chamado "minesweeper_solver.py" para escrita
    with open("minesweeper_solver.py", "w") as file:
        # Escreve importações necessárias no arquivo
        file.write("from minesweeper import Minesweeper\n")
        file.write("import config\n")
        file.write("import tkinter as tk\n")
        file.write("from tkinter import messagebox\n\n")

        # Escreve a definição da classe GUI para o Campo Minado
        file.write("class MinesweeperGUI:\n")
        # Método construtor da classe GUI
        file.write("    def __init__(self, master, game, moves):\n")
        file.write("        self.master = master\n")
        file.write("        self.game = game\n")
        file.write("        self.moves = moves\n")
        # Cria botões para representar o tabuleiro
        file.write("        self.buttons = [[tk.Button(master, width=2, height=1) for _ in range(game.size)] for _ in range(game.size)]\n")
        # Posiciona os botões na janela
        file.write("        for y in range(game.size):\n")
        file.write("            for x in range(game.size):\n")
        file.write("                btn = self.buttons[y][x]\n")
        file.write("                btn.grid(row=y, column=x)\n")
        # Inicia o processo de jogadas
        file.write("        self.next_move()\n\n")
        
        # Método para executar a próxima jogada
        file.write("    def next_move(self):\n")
        # Verifica se ainda há movimentos
        file.write("        if not self.moves:\n")
        # Exibe uma mensagem quando todos os movimentos forem realizados
        file.write("            messagebox.showinfo('Fim', 'Todos os movimentos foram realizados!')\n")
        file.write("            return\n")
        # Executa o próximo movimento e atualiza os botões
        file.write("        move = self.moves.pop(0)\n")
        file.write("        success = self.game.open_cell(*move)\n")
        file.write("        self.update_buttons()\n")
        # Aguarda 500ms antes de fazer o próximo movimento
        file.write("        self.master.after(500, self.next_move)\n\n")
        
        # Método para atualizar o estado dos botões
        file.write("    def update_buttons(self):\n")
        # Atualiza cada botão com o estado atual do jogo
        file.write("        for y in range(self.game.size):\n")
        file.write("            for x in range(self.game.size):\n")
        file.write("                btn = self.buttons[y][x]\n")
        file.write("                if self.game.opened[y][x]:\n")
        file.write("                    btn.config(text=str(self.game.board[y][x]))\n\n")

        # Função para iniciar a solução do Campo Minado
        file.write("def solve():\n")
        # Cria a janela principal
        file.write("    root = tk.Tk()\n")
        # Inicializa o jogo com as configurações
        file.write("    game = Minesweeper(config.BOARD_SIZE, config.NUM_MINES)\n")
        # Inicializa o jogo com as configurações
        file.write("    moves = " + str(best_solution.genome) + "\n")
        # Cria a interface gráfica com o jogo e os movimentos
        file.write("    gui = MinesweeperGUI(root, game, moves)\n")
        # Inicia o loop principal da interface gráfica
        file.write("    root.mainloop()\n\n")

        # Verifica se o script é o principal e executa a solução
        file.write("if __name__ == '__main__':\n")
        file.write("    solve()\n")

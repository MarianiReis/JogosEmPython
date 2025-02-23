import tkinter as tk
from tkinter import messagebox

class JogoDaVelha:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Velha")
        self.jogador_atual = "X"
        self.tabuleiro = [["" for _ in range(3)] for _ in range(3)]
        self.botoes = [[None for _ in range(3)] for _ in range(3)]

        self.criar_interface()

    def criar_interface(self):
        for i in range(3):
            for j in range(3):
                self.botoes[i][j] = tk.Button(self.root, text="", font=("Arial", 20), width=5, height=2,
                                              command=lambda i=i, j=j: self.jogada(i, j))
                self.botoes[i][j].grid(row=i, column=j)

    def jogada(self, i, j):
        if self.tabuleiro[i][j] == "" and not self.verificar_vitoria():
            self.tabuleiro[i][j] = self.jogador_atual
            self.botoes[i][j].config(text=self.jogador_atual, state="disabled")

            if self.verificar_vitoria():
                messagebox.showinfo("Fim de Jogo", f"Jogador {self.jogador_atual} venceu!")
                self.reiniciar_jogo()
            elif self.verificar_empate():
                messagebox.showinfo("Fim de Jogo", "Empate!")
                self.reiniciar_jogo()
            else:
                self.jogador_atual = "O" if self.jogador_atual == "X" else "X"

    def verificar_vitoria(self):
        for i in range(3):
            if all(self.tabuleiro[i][j] == self.jogador_atual for j in range(3)) or \
               all(self.tabuleiro[j][i] == self.jogador_atual for j in range(3)):
                return True
        if all(self.tabuleiro[i][i] == self.jogador_atual for i in range(3)) or \
           all(self.tabuleiro[i][2 - i] == self.jogador_atual for i in range(3)):
            return True
        return False

    def verificar_empate(self):
        return all(self.tabuleiro[i][j] != "" for i in range(3) for j in range(3))

    def reiniciar_jogo(self):
        self.jogador_atual = "X"
        self.tabuleiro = [["" for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.botoes[i][j].config(text="", state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoDaVelha(root)
    root.mainloop()
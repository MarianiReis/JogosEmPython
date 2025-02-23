import tkinter as tk
import random
import time

class JogoDaMemoria:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Memória")
        
        self.simbolos = ["🍎", "🍌", "🍉", "🍇", "🥕", "🍒", "🥑", "🍍"] * 2  # duplica os emojis
        random.shuffle(self.simbolos)  # Embaralha os símbolos
        
        self.botoes = []
        self.primeira_escolha = None
        self.segunda_escolha = None
        
        self.criar_interface()

    def criar_interface(self):
        for i in range(4):
            linha = []
            for j in range(4):
                btn = tk.Button(self.root, text="❓", font=("Arial", 20), width=5, height=2,
                                command=lambda i=i, j=j: self.revelar_carta(i, j))
                btn.grid(row=i, column=j)
                linha.append(btn)
            self.botoes.append(linha)

    def revelar_carta(self, i, j):
        if self.botoes[i][j]["text"] == "❓" and not self.segunda_escolha:
            self.botoes[i][j]["text"] = self.simbolos[i * 4 + j]

            if not self.primeira_escolha:
                self.primeira_escolha = (i, j)
            else:
                self.segunda_escolha = (i, j)
                self.root.after(1000, self.verificar_par)

    def verificar_par(self):
        i1, j1 = self.primeira_escolha
        i2, j2 = self.segunda_escolha

        if self.simbolos[i1 * 4 + j1] == self.simbolos[i2 * 4 + j2]:
            self.botoes[i1][j1]["state"] = "disabled"
            self.botoes[i2][j2]["state"] = "disabled"
        else:
            self.botoes[i1][j1]["text"] = "❓"
            self.botoes[i2][j2]["text"] = "❓"

        self.primeira_escolha = None
        self.segunda_escolha = None

        if all(btn["state"] == "disabled" for linha in self.botoes for btn in linha):
            tk.messagebox.showinfo("Parabéns!", "Você finalizou!")
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    JogoDaMemoria(root)
    root.mainloop()
import tkinter as tk
from tkinter import messagebox
import random


categorias = {
    "Animais": ["elefante", "tigre", "girafa", "jacare", "gato"],
    "Países": ["brasil", "argentina", "alemanha", "canada", "japao"],
    "Tecnologia": ["computador", "programacao", "internet", "algoritmo", "software"]
}

class JogoDaForca:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Forca")
        self.palavra_secreta = ""
        self.letras_corretas = set()
        self.letras_erradas = set()
        self.tentativas = 6

        self.criar_interface()

    def criar_interface(self):
      
        self.label_categoria = tk.Label(self.root, text="Escolha uma categoria:", font=("Arial", 14))
        self.label_categoria.pack(pady=10)

        for categoria in categorias.keys():
            btn = tk.Button(self.root, text=categoria, font=("Arial", 12), command=lambda c=categoria: self.iniciar_jogo(c))
            btn.pack(pady=5)

    def iniciar_jogo(self, categoria):
        self.palavra_secreta = random.choice(categorias[categoria]).upper()
        self.letras_corretas.clear()
        self.letras_erradas.clear()
        self.tentativas = 6

    
        for widget in self.root.winfo_children():
            widget.destroy()

     
        self.label_palavra = tk.Label(self.root, text=self.exibir_palavra(), font=("Arial", 24))
        self.label_palavra.pack(pady=20)

       
        self.label_tentativas = tk.Label(self.root, text=f"Tentativas restantes: {self.tentativas}", font=("Arial", 14))
        self.label_tentativas.pack()

       
        self.frame_letras = tk.Frame(self.root)
        self.frame_letras.pack(pady=10)
        self.botoes_letras = {}
        
        for letra in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            btn = tk.Button(self.frame_letras, text=letra, font=("Arial", 12), width=4, command=lambda l=letra: self.tentar_letra(l))
            btn.grid(row=ord(letra) // 9, column=ord(letra) % 9, padx=3, pady=3)
            self.botoes_letras[letra] = btn

    def exibir_palavra(self):
        return " ".join([letra if letra in self.letras_corretas else "_" for letra in self.palavra_secreta])

    def tentar_letra(self, letra):
        if letra in self.palavra_secreta:
            self.letras_corretas.add(letra)
        else:
            self.letras_erradas.add(letra)
            self.tentativas -= 1

        
        self.label_palavra.config(text=self.exibir_palavra())
        self.label_tentativas.config(text=f"Tentativas restantes: {self.tentativas}")

       
        self.botoes_letras[letra].config(state="disabled")

    
        if all(letra in self.letras_corretas for letra in self.palavra_secreta):
            messagebox.showinfo("Parabéns!", f"Você acertou a palavra: {self.palavra_secreta}")
            self.reiniciar_jogo()
        elif self.tentativas == 0:
            messagebox.showinfo("Game Over!", f"A palavra era: {self.palavra_secreta}")
            self.reiniciar_jogo()

    def reiniciar_jogo(self):
        self.root.destroy()
        root = tk.Tk()
        JogoDaForca(root)
        root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    JogoDaForca(root)
    root.mainloop()
import random
import tkinter as tk
from tkinter import messagebox

# Configuração de palavras
PALAVRAS = ["python", "computador", "hardware", "software", "internet", "mouse",
            "teclado", "hacker", "java", "javascript", "web", "inteligênciaartificial"]


class JogoForca:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Forca")
        self.root.geometry("450x600")
        self.root.configure(bg="#f0f2f5")

        # Variáveis do jogo
        self.palavra = ""
        self.tentativas = 6
        self.letra_descobertas = []
        self.letras_usadas = []

        self.criar_interface()
        self.iniciar_jogo()

    def criar_interface(self):
        # Canvas para desenhar a forca de forma gráfica
        self.canvas = tk.Canvas(self.root, width=200, height=220, bg="white", highlightthickness=1,
                                highlightbackground="#cccccc")
        self.canvas.pack(pady=15)

        # Exibição da palavra oculta
        self.lbl_palavra = tk.Label(self.root, text="", font=("Courier New", 20, "bold"), bg="#f0f2f5", fg="#333333")
        self.lbl_palavra.pack(pady=10)

        # Status de tentativas e letras usadas
        self.lbl_tentativas = tk.Label(self.root, text="", font=("Arial", 11, "bold"), bg="#f0f2f5", fg="#555555")
        self.lbl_tentativas.pack()

        self.lbl_usadas = tk.Label(self.root, text="", font=("Arial", 10, "italic"), bg="#f0f2f5", fg="#777777")
        self.lbl_usadas.pack(pady=5)

        self.lbl_status = tk.Label(self.root, text="", font=("Arial", 12, "bold"), bg="#f0f2f5")
        self.lbl_status.pack(pady=10)

        # Área de entrada
        frame_entrada = tk.Frame(self.root, bg="#f0f2f5")
        frame_entrada.pack(pady=10)

        self.entry_letra = tk.Entry(frame_entrada, font=("Arial", 16), width=4, justify="center")
        self.entry_letra.pack(side=tk.LEFT, padx=5)
        self.entry_letra.bind("<Return>", lambda event: self.verificar_palpite())

        self.btn_enviar = tk.Button(frame_entrada, text="Palpitar", command=self.verificar_palpite,
                                    font=("Arial", 11, "bold"), bg="#4CAF50", fg="white", relief="flat", padx=10)
        self.btn_enviar.pack(side=tk.LEFT, padx=5)

        # Botão Reiniciar
        self.btn_reiniciar = tk.Button(self.root, text="Novo Jogo", command=self.iniciar_jogo,
                                       font=("Arial", 11), bg="#2196F3", fg="white", relief="flat", padx=15)
        self.btn_reiniciar.pack(pady=15)

    def iniciar_jogo(self):
        self.palavra = random.choice(PALAVRAS)
        self.tentativas = 6
        self.letra_descobertas = ["_"] * len(self.palavra)
        self.letras_usadas = []

        self.lbl_status.config(text="Digite uma letra para começar!", fg="#333333")
        self.btn_enviar.config(state=tk.NORMAL)
        self.entry_letra.config(state=tk.NORMAL)
        self.entry_letra.focus()

        self.desenhar_forca()
        self.atualizar_tela()

    def atualizar_tela(self):
        self.lbl_palavra.config(text=" ".join(self.letra_descobertas))
        self.lbl_tentativas.config(text=f"Restam {self.tentativas} tentativas")
        self.lbl_usadas.config(text="Letras usadas: " + ", ".join(self.letras_usadas).upper())

    def desenhar_forca(self):
        self.canvas.delete("all")
        # Estrutura base da forca (sempre visível)
        self.canvas.create_line(30, 200, 150, 200, width=4)  # Base
        self.canvas.create_line(60, 200, 60, 20, width=4)  # Poste vertical
        self.canvas.create_line(60, 20, 130, 20, width=4)  # Poste horizontal
        self.canvas.create_line(130, 20, 130, 50, width=2)  # Corda

        # Desenha as partes do boneco conforme os erros (6 - tentativas remanescentes)
        erros = 6 - self.tentativas
        if erros >= 1: self.canvas.create_oval(115, 50, 145, 80, width=3)  # Cabeça
        if erros >= 2: self.canvas.create_line(130, 80, 130, 140, width=3)  # Corpo
        if erros >= 3: self.canvas.create_line(130, 95, 105, 115, width=3)  # Braço esquerdo
        if erros >= 4: self.canvas.create_line(130, 95, 155, 115, width=3)  # Braço direito
        if erros >= 5: self.canvas.create_line(130, 140, 110, 180, width=3)  # Perna esquerda
        if erros >= 6: self.canvas.create_line(130, 140, 150, 180, width=3)  # Perna direita

    def verificar_palpite(self):
        letra = self.entry_letra.get().lower().strip()
        self.entry_letra.delete(0, tk.END)

        if len(letra) != 1 or not letra.isalpha():
            self.lbl_status.config(text="Digite apenas uma letra!", fg="#d32f2f")
            return
        if letra in self.letras_usadas:
            self.lbl_status.config(text="Você já usou esta letra!", fg="#f57c00")
            return

        self.letras_usadas.append(letra)

        if letra in self.palavra:
            self.lbl_status.config(text="Você acertou! ✅", fg="#388E3C")
            for i in range(len(self.palavra)):
                if self.palavra[i] == letra:
                    self.letra_descobertas[i] = letra
        else:
            self.lbl_status.config(text="Você errou! ❌", fg="#d32f2f")
            self.tentativas -= 1
            self.desenhar_forca()

        self.atualizar_tela()

        # Fim de jogo
        if "_" not in self.letra_descobertas:
            self.lbl_status.config(text="Você venceu!! 🚀", fg="#388E3C")
            messagebox.showinfo("Fim de Jogo", f"Parabéns! Você venceu!\nA palavra era: {self.palavra.upper()}")
            self.finalizar_jogo()
        elif self.tentativas == 0:
            self.lbl_status.config(text="GAME OVER! 💀", fg="#d32f2f")
            messagebox.showerror("Fim de Jogo", f"Você perdeu!\nA palavra era: {self.palavra.upper()}")
            self.finalizar_jogo()

    def finalizar_jogo(self):
        self.btn_enviar.config(state=tk.DISABLED)
        self.entry_letra.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    app = JogoForca(root)
    root.mainloop()

import random
import tkinter as tk
from tkinter import messagebox

# 1. Configuração das palavras
PALAVRAS = ["python", "computador", "hardware", "software", "internet", "mouse",
            "teclado", "hacker", "java", "javascript", "web", "inteligênciaartificial"]

# 2.Lista ASCII art
FORCA = [
"""
+---+
| |
|
|
|
|
=========
""",
"""
+---+
| |
| O 
|
|
|
=========
""",
"""
+---+
| |
| O 
| |
|
|
=========
""",
"""
+---+
| |
| O 
|/|
|
|
=========
""",
r"""
+---+
| |
| O 
|/|\
|
|
=========
""",
r"""
+---+
| |
| O 
|/|\
|/
|
=========
""",
r"""
Game Over!
+---+
| |
| O 
|/|\
|/ \
|
=========
"""
]

# 3. Variáveis globais
palavra_secreta = ""
tentativas = 6
letras_descobertas = []
letras_usadas = []


# 4. Atualiza o desenho com o índice da  lista
def atualizar_desenho_forca():
    erros = 6 - tentativas
    lbl_desenho_forca.config(text=FORCA[erros])


# 5. Atualiza os textos  da tela
def atualizar_tela():
    lbl_palavra.config(text=" ".join(letras_descobertas))
    lbl_tentativas.config(text=f"Restam {tentativas} tentativas")
    lbl_usadas.config(text="Letras usadas: " + ", ".join(letras_usadas).upper())


# 6. Inicia ou reinicia o jogo limpo
def iniciar_jogo():
    global palavra_secreta, tentativas, letras_descobertas, letras_usadas

    palavra_secreta = random.choice(PALAVRAS)
    tentativas = 6
    letras_descobertas = ["_"] * len(palavra_secreta)
    letras_usadas = []

    lbl_status.config(text="Digite uma letra para começar!", fg="#333333")
    btn_enviar.config(state=tk.NORMAL)
    entry_letra.config(state=tk.NORMAL)
    entry_letra.delete(0, tk.END)
    entry_letra.focus()

    atualizar_desenho_forca()
    atualizar_tela()


# 7. Desativa os campos ao encerrar a partida
def finalizar_jogo():
    btn_enviar.config(state=tk.DISABLED)
    entry_letra.config(state=tk.DISABLED)


# 8. Lógica de validação e verificação do palpite
def verificar_palpite():
    global tentativas

    letra = entry_letra.get().lower().strip()
    entry_letra.delete(0, tk.END)

    if len(letra) != 1 or not letra.isalpha():
        lbl_status.config(text="Digite apenas uma letra!", fg="#d32f2f")
        return
    if letra in letras_usadas:
        lbl_status.config(text="Você já usou esta letra!", fg="#f57c00")
        return

    letras_usadas.append(letra)

    if letra in palavra_secreta:
        lbl_status.config(text="Você acertou! ✅", fg="#388E3C")
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                letras_descobertas[i] = letra
    else:
        lbl_status.config(text="Você errou! ❌", fg="#d32f2f")
        tentativas -= 1
        atualizar_desenho_forca()

    atualizar_tela()

    if "_" not in letras_descobertas:
        lbl_status.config(text="Você venceu!! 🚀", fg="#388E3C")
        messagebox.showinfo("Fim de Jogo", f"Parabéns! Você venceu!\nA palavra era: {palavra_secreta.upper()}")
        finalizar_jogo()
    elif tentativas == 0:
        lbl_status.config(text="GAME OVER! 💀", fg="#d32f2f")
        messagebox.showerror("Fim de Jogo", f"Você perdeu!\nA palavra era: {palavra_secreta.upper()}")
        finalizar_jogo()


# 9. Construção da Janela Gráfica
janela = tk.Tk()
janela.title("Jogo da Forca")
janela.geometry("450x650")
janela.configure(bg="#F5F5F5")

# Labels
lbl_desenho_forca = tk.Label(janela, text="", font=("Courier New", 14), bg="white",
                             fg="black", width=15, height=9, relief="solid", bd=1, justify="left")
lbl_desenho_forca.pack(pady=15)

lbl_palavra = tk.Label(janela, text="", font=("Courier New", 20, "bold"), bg="#E5E5E5", fg="#333333")
lbl_palavra.pack(pady=10)

lbl_tentativas = tk.Label(janela, text="", font=("Arial", 11, "bold"), bg="#E5E5E5", fg="#555555")
lbl_tentativas.pack()

lbl_usadas = tk.Label(janela, text="", font=("Arial", 10, "italic"), bg="#f0f2f5", fg="#777777")
lbl_usadas.pack(pady=5)

lbl_status = tk.Label(janela, text="", font=("Arial", 12, "bold"), bg="#E5E5E5")
lbl_status.pack(pady=10)

frame_entrada = tk.Frame(janela, bg="#f0f2f5")
frame_entrada.pack(pady=10)

entry_letra = tk.Entry(frame_entrada, font=("Arial", 16), width=4, justify="center")
entry_letra.pack(side=tk.LEFT, padx=5)
janela.bind("<Return>", lambda event: verificar_palpite())

btn_enviar = tk.Button(frame_entrada, text="Palpitar", command=verificar_palpite,
                       font=("Arial", 11, "bold"), bg="#4CAF50", fg="white", relief="flat", padx=10)
btn_enviar.pack(side=tk.LEFT, padx=5)

btn_reiniciar = tk.Button(janela, text="Novo Jogo", command=iniciar_jogo,
                          font=("Arial", 11), bg="#2196F3", fg="white", relief="flat", padx=15)
btn_reiniciar.pack(pady=15)

# 10. Executa o jogo
iniciar_jogo()
janela.mainloop()

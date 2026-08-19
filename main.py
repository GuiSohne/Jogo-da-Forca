# 1. Importações para a aplicação
import random
import tkinter as tk
from tkinter import messagebox

# 2. Configuração das palavras usadas no jogo da forca
PALAVRAS = ["python", "computador", "hardware", "software", "internet", "mouse",
            "teclado", "hacker", "java", "javascript", "web", "inteligênciaartificial"]

# 3. Lista de arte em ASCII 
FORCA = [
    """
    +---+
    |¯¯|
    |
    |
    |
    |
    |
    ==========
    """,
    """
    +---+
    |¯¯|
    |  O 
    |
    |
    |
    |
    ==========
    """,
    """
    +---+
    |¯¯|
    |  O 
    |  |
    |
    |
    |
    ==========
    """,
    """
    +---+
    |¯¯|
    |  O 
    | /|
    |
    |
    |
    ==========
    """,
    r"""
    +---+
    |¯¯|
    |  O 
    | /|\
    |
    |
    |
    ==========
    """,
    r"""
    +---+
    |¯¯|
    |  O 
    | /|\
    | /
    |
    |
    ==========
    """,
    r"""
    Game Over!
    +---+
    | ||
    |  O 
    | /|\
    | / \
    |
    |
    ==========
    """
]

# 4. Variáveis globais, armazena os estados do jogo
palavra_secreta = ""
tentativas = 6
letras_descobertas = []
letras_usadas = []


# 5. Atualiza o desenho com o índice da  lista de acordo com os erros
def atualizar_desenho_forca():
    erros = 6 - tentativas
    lbl_desenho_forca.config(text=FORCA[erros])


# 6. Atualiza os textos  da tela, tanto os descobertos quanto os restantes
def atualizar_tela():
    lbl_palavra.config(text=" ".join(letras_descobertas))
    lbl_tentativas.config(text=f"Restam {tentativas} tentativas")
    lbl_usadas.config(text="Letras usadas: " + ", ".join(letras_usadas).upper())


# 7. Inicia ou reinicia o jogo limpo
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


# 8. Desativa os campos ao acabar o jogo
def finalizar_jogo():
    btn_enviar.config(state=tk.DISABLED)
    entry_letra.config(state=tk.DISABLED)


# 9. Validação e verificação da letra
def verificar_palpite():
    global tentativas

    letra = entry_letra.get().lower().strip()  # Pega a letra digitada, colocando ela em minúsculo e tirando algum espaço
    entry_letra.delete(0, tk.END)

    # 10. Se o usuário digitou apenas uma letra, ou se é a mesma
    if len(letra) != 1 or not letra.isalpha():
        lbl_status.config(text="Digite apenas uma letra!", fg="#d32f2f")
        return
    if letra in letras_usadas:
        lbl_status.config(text="Você já usou esta letra!", fg="#f57c00")
        return

    # 11. adiciona a letra para a lista, adicionando nas letras descobertas e caso erre, diminuindo tentativas
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


# 12. Configuração da janela Tkinter e configuração para coloca-lá no meio da tela do usuário
janela = tk.Tk()
janela.title("Jogo da Forca")

# Tamanho da janela
largura = 450
altura = 650
# Pega o tamanho da tela do computador
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
# Calcula a posição para o meio
posx = int(largura_tela / 2 - largura / 2)
posy = int(altura_tela / 2 - altura / 2)
# Define o tamanho e a posição (LxA+X+Y)
janela.geometry(f"{largura}x{altura}+{posx}+{posy}")
janela.configure(bg="#F5F5F5")

# Componentes para visual
lbl_desenho_forca = tk.Label(janela, text="", font=("Courier New", 14), bg="#6D8196",
                             fg="black", width=15, height=9, relief="solid", bd=1, justify="left")
lbl_desenho_forca.pack(pady=15)

lbl_palavra = tk.Label(janela, text="", font=("Courier New", 20, "bold"), bg="#DDE4EC", fg="#333333")
lbl_palavra.pack(pady=10)

lbl_tentativas = tk.Label(janela, text="", font=("Arial", 11, "bold"), bg="#F5F5F5", fg="#555555")
lbl_tentativas.pack()

lbl_usadas = tk.Label(janela, text="", font=("Arial", 10, "italic"), bg="#F5F5F5", fg="#777777")
lbl_usadas.pack(pady=5)

lbl_status = tk.Label(janela, text="", font=("Arial", 12, "bold"), bg="#F5F5F5")
lbl_status.pack(pady=10)

frame_entrada = tk.Frame(janela, bg="#f0f2f5")
frame_entrada.pack(pady=10)

entry_letra = tk.Entry(frame_entrada, font=("Arial", 16), width=4, justify="center")
entry_letra.pack(side=tk.LEFT, padx=5)
janela.bind("<Return>", lambda event: verificar_palpite())

btn_enviar = tk.Button(frame_entrada, text="Palpitar", command=verificar_palpite,
                       font=("Arial", 11, "bold"), bg="#ADD8E6", fg="black", relief="flat", padx=10)
btn_enviar.pack(side=tk.LEFT, padx=5)

btn_reiniciar = tk.Button(janela, text="Novo Jogo", command=iniciar_jogo,
                          font=("Arial", 11), bg="#4CAF50", fg="white", relief="flat", padx=15)
btn_reiniciar.pack(pady=15)

# 13. Iniciar o jogo
iniciar_jogo()
janela.mainloop()
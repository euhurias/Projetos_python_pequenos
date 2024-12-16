import customtkinter

customtkinter.set_appearance_mode("dark")

def cadastrar_filme():
    resposta.configure(text="Cadastrado com sucesso!")

# criando janela
janela = customtkinter.CTk()
janela.title("Tela Interativa")
janela.geometry("600x380")


titulo = customtkinter.CTkLabel(janela, text="Cadastros de filmes", font=("Arial", 14, "bold"))
titulo.pack(pady=20)

filme = customtkinter.CTkLabel(janela, text="Filme")
filme.pack()

filmetxt = customtkinter.CTkEntry(janela)
filmetxt.pack()

ator = customtkinter.CTkLabel(janela, text="Ator")
ator.pack()

atortxt = customtkinter.CTkEntry(janela)
atortxt.pack()

genero = customtkinter.CTkLabel(janela, text="Genero do filme")
genero.pack(pady=20)

generoquadro = customtkinter.CTkFrame(janela)
generoquadro.pack()

generoacao = customtkinter.CTkCheckBox(generoquadro, text="Ação")
generoacao.pack(side = "left")
generodrama = customtkinter.CTkCheckBox(generoquadro, text="Drama")
generodrama.pack(side = "left")
generocomedia = customtkinter.CTkCheckBox(generoquadro, text="Comédia")
generocomedia.pack(side = "left")
generocrime = customtkinter.CTkCheckBox(generoquadro, text="True Crime")
generocrime.pack(side = "left")

button = customtkinter.CTkButton(janela, text="Cadastrar", command=cadastrar_filme)
button.pack(pady=20)

resposta = customtkinter.CTkLabel(janela, text=" ")
resposta.pack()


janela.mainloop()
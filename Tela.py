import customtkinter

# criando janela
janela = customtkinter.CTk()
janela.title("Tela Interativa")
janela.geometry("600x380")


titulo = customtkinter.CTkLabel(janela, text="Cadastros de filmes", font=("Arial", 14, "bold"))
titulo.pack(pady=20)

filme = customtkinter.CTkLabel(janela, text="Filme")
filme.pack(pady=20)

janela.mainloop()
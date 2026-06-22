import customtkinter as ctk
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
root = ctk.CTk()
root.geometry("1200x700")
root.resizable(False,False)

#####################################################################
def menu():
    root.configure(fg_color="white")
    framelob = ctk.CTkFrame(root, fg_color="#0088ff")
    framelob.place(relx=0.5,rely=0.01,relheight=0.15,relwidth=1,anchor="center")
    title = ctk.CTkLabel(framelob,text="Super Mercado Normal (e super)", text_color="#f6ff00", font=("Gill Sans MT Condensed", 23,"bold"))
    title.place(relx=0.15,rely=0.7,anchor = "center")
    ctk.CTkLabel(framelob, text="🛒R$∞", text_color="white", font=("Arial", 28, "bold")).place(relx=0.92,rely=0.75,anchor="center")

    compras = ctk.CTkButton(root, text="Produtos",text_color="black", font=("Arial", 28, "bold"),command=compra)
    compras.place(relx=0.25,rely=0.35,anchor="center")
def compra():
    for item in root.winfo_children():
        item.destroy()
    framelob = ctk.CTkFrame(root, fg_color="#0088ff")
    framelob.place(relx=0.5, rely=0.01, relheight=0.15, relwidth=1, anchor="center")
    title = ctk.CTkLabel(framelob, text="Super Mercado Normal (e super)", text_color="#f6ff00",
                         font=("Gill Sans MT Condensed", 23, "bold"))
    title.place(relx=0.15, rely=0.7, anchor="center")
    ctk.CTkLabel(framelob, text="🛒R$∞", text_color="white", font=("Arial", 28, "bold")).place(relx=0.92, rely=0.75,anchor="center")
    lista_compras = []
    def adicionar_ao_carrinho(nome_produto):
        lista_compras.append(nome_produto)
        print(f"Adicionado: {nome_produto}")
        print(f"Lista atual: {lista_compras}")
    nomes_produtos = [
        "Beterraba", "Beterraba", "Beterraba", "Beterraba", "Beterraba",
        "Beterraba", "Beterraba", "Beterraba", "Beterraba", "Beterraba",
        "Beterraba", "Beterraba", "Beterraba", "Beterraba", "Beterraba",
        "Beterraba", "Beterraba", "Resistor", "Beterraba", "Beterraba"
    ]
    posicoes_x = [0.1, 0.23, 0.36, 0.49, 0.62]
    posicoes_y = [0.2, 0.35, 0.5, 0.65]
    botoes = []
    contador = 0
    for y in posicoes_y:
        for x in posicoes_x:
            if contador < len(nomes_produtos):
                nome_atual = nomes_produtos[contador]
            else:
                nome_atual = f"Produto {contador + 1}"
            compras = ctk.CTkButton(root, text=nome_atual, text_color="black", font=("Arial", 18, "bold"), command=lambda p=nome_atual: adicionar_ao_carrinho(p))
            compras.place(relx=x, rely=y, relheight=0.12, relwidth=0.12, anchor="center")
            botoes.append(compras)
            contador += 1

    ctk.CTkFrame(root,fg_color="#dadbbd").place(relx=0.85, rely=0.5,relheight=0.7,relwidth=0.27,anchor="center")
    ctk.CTkLabel(root, text="Lista de Compras",text_color="black",fg_color="#dadbbd",font=("Arial",20,"bold")).place(relx=0.85, rely=0.2,anchor="center")


menu()
root.mainloop()
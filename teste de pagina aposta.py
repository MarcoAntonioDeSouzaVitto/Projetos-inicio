import random
import tkinter as tk
import sqlite3

name_user = "Guest"
saldo = 0
janela = tk.Tk()
janela.title("GRANDE_ONÇÃO")
janela.minsize(width=900, height=700)
conexao = sqlite3.connect("dadosonca1.db")
funcio = conexao.cursor()
funcio.execute("""
    CREATE TABLE IF NOT EXISTS bancoDeDados(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    saldo REAL NOT NULL
)
""")
def menu():
    for elementos in janela.winfo_children():
        elementos.destroy()
    janela.config(bg="#121212")
    # =====~Frame~===========----------
    frame_menu = tk.Frame(janela, bg="#cc1212")
    frame_menu.place(relx=0.5,rely=0.1,relwidth=1,relheight=0.2,anchor="center")
    # =====~Title~===========----------
    tk.Label(frame_menu,text="GRANDE ONÇÃO🐆🎲",font=("Palatino Linotype", 24, "bold"), bg="#cc1212",fg="#F5F5F7").place(relx=0.5,rely=0.5,anchor="center")
    #=====~Login~===========----------
    login_button = tk.Button(janela,text="LOGIN",bg="#FFCE00", font=("Georgia", 12),command= login)
    login_button.place(relx=0.5,rely=0.4,relwidth=0.2,relheight=0.075, anchor="center")
    #=====~Register~===========----------
    register_button = tk.Button(janela,text="REGISTER",bg="#12E06A", font=("Georgia", 12), command=cadastro)
    register_button.place(relx=0.5,rely=0.6,relwidth=0.2,relheight=0.075, anchor="center")
    # =====~Selo~===========----------
    tk.Label(janela, text="⋈ SELO DE HONESTIDADE DA O.N.U ⋈", bg="#121212", fg="#F5F5F7", font=("Arial", 10, "bold")).place(relx=0.02,rely=0.95)

    #~~~~~~EXCLOI~~~~~~~~~~~~~~~~
    tk.Button(janela,text="Pular",command=lets_go_gambling).place(relx=0.1,rely=0.9)


def login():
    for elementos in janela.winfo_children():
        elementos.destroy()
    janela.config(bg="#403f3e")
    def pegar_dados():
        global name_user, saldo, email_user
        e = email_entry.get().strip()
        p = password_entry.get().strip()
        funcio.execute("SELECT email, password FROM bancoDeDados WHERE email = ? AND password = ?",(e,p))
        busca = funcio.fetchall()
        if not busca:
            msg = "INCORRET EMAIL OR PASSWORD"
            aviso = tk.Label(frame_menu, text=msg, bg="#222626", fg="red", font=("arial", 12, "bold"))
            aviso.place(relx=0.5, rely=0.59, anchor="center")
        else:
            funcio.execute("SELECT username,saldo from bancoDeDados WHERE email = ?", (e,))
            resultado = funcio.fetchone()
            name_user = resultado[0]
            email_user = e
            saldo = resultado[1]
            lets_go_gambling()

    # =====~Frame~===========----------
    frame_menu = tk.Frame(janela, bg="#222626")
    frame_menu.place(relx=0.73,rely=0.5,relwidth=0.5,relheight=0.95,anchor="center")
    # =====~Email~===========----------
    emailLogin = tk.Label(frame_menu, text="Email", bg ="#222626", fg="white" )
    emailLogin.place(relx=0.14, rely=0.25, anchor="center")
    email_entry = tk.Entry(frame_menu, highlightbackground="black", highlightthickness=2, font=("Arial", 14))
    email_entry.place(relx=0.5,rely=0.3,relwidth=0.8,relheight=0.08,anchor="center")
    # =====~Password~===========----------
    passwordLogin = tk.Label(frame_menu, text="Password", bg ="#222626", fg="white" )
    passwordLogin.place(relx=0.16, rely=0.45, anchor="center")
    password_entry= tk.Entry(frame_menu, highlightbackground="black", highlightthickness=2, font=("Arial", 14), show="*")
    password_entry.place(relx=0.5,rely=0.5,relwidth=0.8,relheight=0.08,anchor="center")
    # =====~Send~===========----------
    send_button = tk.Button(frame_menu, text="Send", command=pegar_dados)
    send_button.place(relx=0.5,rely=0.68,relwidth=0.5,relheight=0.08, anchor="center")

    tk.Label(janela, text="Login", bg="#222626", fg="White", font=("Agency FB", 28,"bold")).place(relx=0.73, rely=0.08, anchor="center")
    tk.Label(janela, text="🐯", bg="#403f3e", fg="#ffd900", font=("Arial", 90)).place(relx=0.23, rely=0.5,anchor="center")
    tk.Label(janela, text="O N Ç A", bg="#403f3e", fg="#ffd900", font=("Arial", 50)).place(relx=0.23, rely=0.37,anchor="center")
    tk.Button(janela,text="Back", command=menu).place(relx=0.04,rely=0.9)


def cadastro():
    global email_user
    for elementos in janela.winfo_children():
        elementos.destroy()
    janela.config(bg="#403f3e")

    def pegar_dados():
        global name_user, saldo
        u = username_entry.get()
        e = email_entry.get()
        p = password_entry.get()
        pc = passwordConfirm_entry.get()
        saldo = 0
        msg = ""
        if u == "" or e == "" or p == "" or pc == "":
            msg = "FILL IN ALL FIELDS"
        elif not e.endswith(("@gmail.com", "@outlook.com", "@yahoo.com", "@hotmail.com")):
            msg = "ENTER A VALID EMAIL"
        elif p != pc:
            msg = "PASSWORDS DO NOT MATCH"
        elif len(p) < 6:
            msg = "ENTER A VALID PASSWORD"
        if msg == "":
            funcio.execute("SELECT email FROM bancoDeDados WHERE email = ?", (e,))
            search = funcio.fetchone()
            if not search is None:
                msg = "EMAIL JÁ CADASTRADO NO SISTEMA!"
        if msg != "":
            aviso = tk.Label(frame_menu, text=msg, fg="red", bg="#222626", font=("Arial", 12, "bold"))
        else:
            aviso = tk.Label(frame_menu, text="CADASTRO REALIZADO COM SUCESSO!", fg="green", bg="#222626",font=("Arial", 12, "bold"))
            funcio.execute("""INSERT INTO bancoDeDados(username, email, password, saldo)VALUES (?, ?, ?,?)""", (u, e, p, saldo))
            name_user = u
            email_user = e
            menu()
            conexao.commit()
        aviso.place(relx=0.5, rely=0.715, anchor="center")
    # =====~Frame~===========----------
    frame_menu = tk.Frame(janela, bg="#222626")
    frame_menu.place(relx=0.73,rely=0.5,relwidth=0.5,relheight=0.95,anchor="center")
    # =====~Username~===========----------
    usernameLogin = tk.Label(frame_menu, text="Username", bg ="#222626", fg="white" )
    usernameLogin.place(relx=0.18, rely=0.19, anchor="center")
    username_entry = tk.Entry(frame_menu, highlightbackground="black", highlightthickness=2, font=("Arial", 14))
    username_entry.place(relx=0.5,rely=0.24,relwidth=0.75,relheight=0.08,anchor="center")
    # =====~Email~===========----------
    emailLogin = tk.Label(frame_menu, text="Email", bg ="#222626", fg="white" )
    emailLogin.place(relx=0.16, rely=0.32, anchor="center")
    email_entry = tk.Entry(frame_menu, highlightbackground="black", highlightthickness=2, font=("Arial", 14))
    email_entry.place(relx=0.5,rely=0.37,relwidth=0.75,relheight=0.08,anchor="center")
    # =====~Password~===========----------
    passwordLogin = tk.Label(frame_menu, text="Password", bg ="#222626", fg="white" )
    passwordLogin.place(relx=0.18, rely=0.45, anchor="center")
    password_entry= tk.Entry(frame_menu, highlightbackground="black", highlightthickness=2, font=("Arial", 14), show="*")
    password_entry.place(relx=0.5,rely=0.5,relwidth=0.75,relheight=0.08,anchor="center")
    # =====~Password_Confirm~===========----------
    passwordConfirmLogin = tk.Label(frame_menu, text="Password Confirm", bg ="#222626", fg="white" )
    passwordConfirmLogin.place(relx=0.23, rely=0.58, anchor="center")
    passwordConfirm_entry= tk.Entry(frame_menu, highlightbackground="black", highlightthickness=2, font=("Arial", 14), show="*")
    passwordConfirm_entry.place(relx=0.5,rely=0.63,relwidth=0.75,relheight=0.08,anchor="center")
    # =====~Send~===========----------
    send_button = tk.Button(frame_menu, text="Send", command=pegar_dados)
    send_button.place(relx=0.5,rely=0.8,relwidth=0.5,relheight=0.08, anchor="center")
    tk.Label(janela, text="Create Account", bg="#222626", fg="White", font=("Agency FB", 28,"bold")).place(relx=0.73, rely=0.08, anchor="center")
    tk.Label(janela, text="🐯", bg="#403f3e", fg="#ffd900", font=("Arial", 90)).place(relx=0.23, rely=0.5,anchor="center")
    tk.Label(janela, text="O N Ç A", bg="#403f3e", fg="#ffd900", font=("Arial", 50)).place(relx=0.23, rely=0.37,anchor="center")

    tk.Button(janela,text="Back", command=menu).place(relx=0.04,rely=0.9)

def deposito():
    global email_user, saldo
    for elementos in janela.winfo_children():
        elementos.destroy()
    janela.config(bg="#403f3e")
    # =====~Frame~===========----------
    frame_menu = tk.Frame(janela, bg="#cc1212")
    frame_menu.place(relx=0.5,rely=0.05,relwidth=1,relheight=0.15,anchor="center")
    # =====~Principal Menu~===========----------
    tk.Label(frame_menu, text="Grande\nOnção", bg="#cc1212",fg="white", font=("Agency FB", 24, "bold")).place(relx=0.1,rely=0.55, anchor="center")
    ola = tk.Label(frame_menu,text=f"Hello, {name_user} 🐯!",bg="#cc1212",fg="white", font=("Arial", 10, "bold"))
    ola.place(relx=0.75,rely=0.3)
    saldo_labeldep = tk.Label(frame_menu,text=f"R$ {saldo:.2f}",bg="#cc1212", fg= "gold", font=("Arial", 15))
    saldo_labeldep.place(relx=0.75,rely=0.5)
    # =====~Comando~===========----------
    def add10():
        global saldo
        saldo += 10
        saldo_labeldep.config(text=f"R$ {saldo:.2f}")
        funcio.execute("UPDATE bancoDeDados SET saldo = ? WHERE email = ?",(saldo, email_user))
        conexao.commit()
    def add50():
        global saldo
        saldo += 50
        saldo_labeldep.config(text=f"R$ {saldo:.2f}")
        funcio.execute("UPDATE bancoDeDados SET saldo = ? WHERE email = ?",(saldo, email_user))
        conexao.commit()

    def add100():
        global saldo
        saldo += 100
        saldo_labeldep.config(text=f"R$ {saldo:.2f}")
        funcio.execute("UPDATE bancoDeDados SET saldo = ? WHERE email = ?",(saldo, email_user))
        conexao.commit()


    ten = tk.Button(janela, text="R$ 10,00", command=add10)
    ten.place(relx=0.4,rely=0.5,anchor="center")
    fifty = tk.Button(janela, text="R$ 50,00", command=add50)
    fifty.place(relx=0.5,rely=0.5,anchor="center")
    hundred = tk.Button(janela, text="R$ 100,00", command=add100)
    hundred.place(relx=0.6,rely=0.5,anchor="center")
    tk.Button(janela, text="Voltar para o Jogo", command=lets_go_gambling, bg="white").place(relx=0.05, rely=0.9)


def lets_go_gambling():
    global name_user, saldo,deposito
    for elementos in janela.winfo_children():
        elementos.destroy()
    janela.config(bg="#403f3e")
    # =====~Frame~===========----------
    frame_menu = tk.Frame(janela, bg="#cc1212")
    frame_menu.place(relx=0.5,rely=0.05,relwidth=1,relheight=0.15,anchor="center")
    # =====~Principal Menu~===========----------
    tk.Label(frame_menu, text="Grande\nOnção", bg="#cc1212",fg="white", font=("Agency FB", 24, "bold")).place(relx=0.1,rely=0.55, anchor="center")
    ola = tk.Label(frame_menu,text=f"Hello, {name_user} 🐯!",bg="#cc1212",fg="white", font=("Arial", 10, "bold"))
    ola.place(relx=0.75,rely=0.3)
    saldo_label = tk.Label(frame_menu,text=f"R$ {saldo:.2f}",bg="#cc1212", fg= "gold", font=("Arial", 15))
    saldo_label.place(relx=0.75,rely=0.5)
    botaodeposito = tk.Button(frame_menu, text="Depósito", fg="black", bg="lightyellow",font=("Arial",12),command=deposito)
    botaodeposito.place(relx=0.9,rely=0.5)
    resultado = 0
    # =====~Jogo ~===========----------
    emojis = ["🐯","🐉","🐙"]
    numbers = []
    randomA = "⬛"
    randomB = "⬛"
    randomC = "⬛"
    visor = tk.Frame(janela, bg="#262626", highlightthickness= 2, highlightcolor="white")
    visor.place(relx=0.5, rely=0.45,relwidth=0.4,relheight=0.12,anchor="center")
    def aposta():
        global randomA, randomB, randomC, resultado, saldo, texto, valor
        if resultado == 1 and valor <= saldo and valor > 0:
            saldo -= valor
            saldo_label.config(text=f"R$ {saldo:.2f}")
            numbers.clear()
            cont = 0
            for i in range(3):
                num = random.randint(1,3)
                numbers.append(num)
            for i in numbers:
                cont += 1
                if i == 1:
                    if cont == 1:
                        randomA = "🐯"
                        p1.config(text=randomA, fg="orange")
                    if cont == 2:
                        randomB = "🐯"
                        p2.config(text=randomB, fg="orange")
                    if cont == 3:
                        randomC = "🐯"
                        p3.config(text=randomC, fg="orange")
                if i == 2:
                    if cont == 1:
                        randomA = "🐉"
                        p1.config(text=randomA, fg="green")
                    if cont == 2:
                        randomB = "🐉"
                        p2.config(text=randomB, fg="green")
                    if cont == 3:
                        randomC = "🐉"
                        p3.config(text=randomC, fg="green")
                if i == 3:
                    if cont == 1:
                        randomA = "🐙"
                        p1.config(text=randomA, fg="red")
                    if cont == 2:
                        randomB = "🐙"
                        p2.config(text=randomB, fg="red")
                    if cont == 3:
                        randomC = "🐙"
                        p3.config(text=randomC, fg="red")
            if numbers[0] == numbers[1] == numbers[2]:
                saldo += (valor_da_aposta*4)
                saldo_label.config(text=f"R$ {saldo:.2f}")
            resultado = 0
    p1 = tk.Label(janela, text=f"{randomA}", bg="#262626", font=("Arial", 24))
    p2 = tk.Label(janela, text=f"{randomB}", bg="#262626", font=("Arial", 24))
    p3 = tk.Label(janela, text=f"{randomC}", bg="#262626", font=("Arial", 24))
    p1.place(relx=0.4, rely=0.45, anchor="center")
    p2.place(relx=0.5, rely=0.45,anchor="center")
    p3.place(relx=0.6, rely=0.45,anchor="center")

    botao = tk.Button(janela, text="ROLL", bg="#12E06A", command=aposta)
    botao.place(relx=0.5,rely=0.75,relwidth=0.2,relheight=0.08,anchor="center")

    def validar(texto):
        if texto == "" or texto == ".":
            return True
        if texto.replace(".", "", 1).isdigit():
            if "." in texto:
                return len(texto.split(".")[1]) <= 2
            return True
        return False
    validacao = janela.register(validar)
    """def lancar_valor():
        global resultado, texto
        texto = valor_aposta.get()
        if texto and texto != ".":
            valor = float(texto)
            if valor <= saldo:
                valor_selecionado.config(text=f"R$ {valor:.2f}")
                resultado = 1"""

    def lancar_valor():
        global valor, texto
        texto = valor_aposta.get()
        if texto and texto != ".":
            valor = float(texto)
            if valor <= saldo:
                valor_selecionado.config(text=f"R$ {valor:.2f}")

    valor_aposta = tk.Entry(janela,validate="key", validatecommand=(validacao, "%P"), bg="white", highlightcolor="black", highlightthickness=0.2, font=("Arial", 20))
    valor_aposta.place(relx=0.5,rely=0.6,anchor="center")

    tk.Label(janela,text="Insira valor",bg="#403f3e", fg="white", font=("Arial", 12)).place(relx=0.5,rely=0.55,anchor="center")

    send_aposta = tk.Button(janela, text="➡️", bg="white", activebackground="#dee1e3", command=lancar_valor)
    send_aposta.place(relx=0.6455,rely=0.6,anchor="center")

    valor_selecionado = tk.Label(janela,text="R$ 0.00",font=("Arial",20,"bold"))
    valor_selecionado.place(relx=0.5,rely=0.3,anchor="center")

menu()
janela.mainloop()
conexao.close()

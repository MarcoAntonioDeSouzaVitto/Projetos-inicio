import json
import os
from datetime import datetime
print("ATM")
extrato = []
dinheiro_atual = [100, 50, 20, 10, 5, 1]
retiradas = []
carteira = 0
if os.path.exists("extrato.json"):
    with open("extrato.json", "r", encoding="utf-8") as f:
        try:
            dados_carregados = json.load(f)
            carteira = dados_carregados["carteira"]
            extrato = dados_carregados["historico"]
        except (json.JSONDecodeError,KeyError):
            extrato = []
            carteira = 0
dados_banco = {
    "carteira": carteira,
    "historico": extrato
}
################################################################################

def visualizar():
    if os.path.exists("extrato.json"):
        with open("extrato.json","r", encoding="utf-8") as f:
            dados = json.load(f)
        print("========== EXTRATO ==========\n")
        for i in dados["historico"]:
            print(i)
        print("\n========== ------- ==========")
    else:
        print("\nNenhum extrato encontrado.")

def deposito():
    global carteira
    while True:
        print(f"——SALDO ATUAL: R${carteira:.2f}——")
        valor = float(input("Valor do Depósito: "))
        if valor >= 1:
            blank = valor
            hora_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            extrato.append(f"{hora_atual} | +R${valor} |")
            for nota in dinheiro_atual:
                while valor >= nota:
                    retiradas.append(nota)
                    valor -= nota
            print(f"→ Depósito de R${blank:.2f} efetuado.\n")
            carteira += blank
            dados_banco["carteira"] = carteira
            with open("extrato.json", "w", encoding="utf-8") as f:
                json.dump(dados_banco, f, indent=4, ensure_ascii=False)
            return
        print("!INSIRA VALOR VÁLIDO PARA SAQUE!")
def sacar():
    global carteira
    print(f"——SALDO ATUAL: R${carteira:.2f}——")
    while True:
        valor = float(input("Valor do Saque: "))
        if valor < 1:
            print("!INSIRA VALOR VÁLIDO PARA SAQUE!")
        elif valor <= carteira:
            blank = valor
            hora_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            extrato.append(f"{hora_atual} | -R${valor} |")
            for nota in dinheiro_atual:
                while valor >= nota:
                    retiradas.append(nota)
                    valor -= nota
            print(f"→ Saque de R${blank:.2f} efetuado.\n")
            carteira -= blank
            dados_banco["carteira"] = carteira
            with open("extrato.json", "w", encoding="utf-8") as f:
                json.dump(dados_banco, f, indent=4, ensure_ascii=False)
            return
        else:
            print("!VALOR MAIOR QUE SALDO ATUAL!")

################################################################################

while True:
    print("| [1] Ver Saldo e Extrato |  [2] Depositar |  [3] Sacar |  [4] Sair | ")
    action = int(input("Ação: ").strip())
    if action == 1:
        visualizar()
    elif action == 2:
        deposito()
    elif action == 3:
        sacar()
    elif action == 4:
            break
    else:
        print("!AÇÃO INEXISTENTE!")

import json
from datetime import datetime
def adicionar():
    print("\n--==Nome da Tarefa==--")
    nome = str(input("Tarefa: "))
    print("\n--==Categoria==--")
    categoria = str(input("Categoria: "))
    print("\n--==Status==--")
    status = str(input("Pendente/Concluída: "))
    hora_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    dados.append([nome,categoria,status,hora_atual])

def alterar():
    print("\n")
    print("--== Dados Salvos ==--")
    for indice, tarefa in enumerate(dados):
        print(f"[{indice}] {tarefa[0]} ({tarefa[1]}) - Status: {tarefa[2]} | {tarefa[3]}")
    mudar = int(input("\n[1] Remover | [2] Substituir\nAção: "))
    if mudar == 1:
        choseX = int(input("Posição X dos Itens: "))
        try:
            remover = dados.pop(choseX)
            print(f"\nTarefa '{remover[0]}' removida com sucesso!")
        except (ValueError, IndexError):
            print("\nNúmero inválido! Nenhuma tarefa foi removida.")
    if mudar == 2:
        choseY = int(input("Posição dos Itens á alterar: "))
        print("\nO que você deseja alterar?")
        print("[0] Apenas o Nome")
        print("[1] Apenas a Categoria")
        print("[2] Apenas o Status")
        print("[3] Tudo")
        coluna = int(input("Opção: "))
        if coluna == 0:
            nome_novo = str(input("Novo nome: "))
            dados[choseY][0] = nome_novo
        if coluna == 1:
            categoria_novo = str(input("Nova categoria: "))
            dados[choseY][1] = categoria_novo
        if coluna == 2:
            status_novo = str(input("Novo status: "))
            dados[choseY][2] = status_novo
        if coluna == 3:
            nome_novo = str(input("Novo nome: "))
            dados[choseY][0] = nome_novo
            categoria_novo = str(input("Nova categoria: "))
            dados[choseY][1] = categoria_novo
            status_novo = str(input("Novo status: "))
            dados[choseY][2] = status_novo
            hora_nova = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            dados[choseY][3] = hora_nova
            print("DADOS ALTERADOS COM SUCESSO!")

def visualizar():
    if not dados:
        print("\nNenhuma tarefa cadastrada")
        return
    print("\n--== Lista de Tarefas ==--")
    for indice, tarefa in enumerate(dados):
        print(f"[{indice}] {tarefa[0]} ({tarefa[1]}) - Status: {tarefa[2]} | {tarefa[3]}")

def salvar():
     with open("dados.json", "w", encoding="utf-8") as f:
         json.dump(dados,f,indent=4,ensure_ascii=False)
     print("SALVO COM SUCESSO!")
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

dados = [
    ["Estudar Python", "Estudos", "Pendente", "20/06/2026 12:00:00"],
    ["Comprar leite", "Mercado", "Pendente", "20/06/2026 12:00:00"]
]
while True:
    print("\n--==Lista de Tarefas==--")
    print(" [1]Adicionar Tarefa\n [2]Alterar Tarefa\n [3]Visualizar\n [4]Salvar")
    acao = int(input("Ação: "))
    if acao == 1:
        adicionar()
        print("Dados Salvos Com Sucesso!")
    if acao == 2:
        alterar()
    if acao == 3:
        visualizar()
    if acao == 4:
        salvar()


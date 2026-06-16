def adicionar():
    global i
    dados.append([])
    i += 1
    print("\n--==Nome da Tarefa==--")
    nome = str(input("Tarefa: "))
    dados[i].append(nome)
    print("\n--==Categoria==--")
    categoria = str(input("Categoria: "))
    dados[i].append(categoria)
    print("\n--==Status==--")
    status = str(input("Pendente/Concluída: "))
    dados[i].append(status)
def alterar():
    print("\n")
    print("--== Dados Salvos ==--")
    for indice, tarefa in enumerate(dados):
        print(f"[{indice}] {tarefa[0]} ({tarefa[1]}) - Status: {tarefa[2]}")
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
            print("DADOS ALTERADOS COM SUCESSO!")
def visualizar():
    for indice, tarefa in enumerate(dados):
        print(f"[{indice}] {tarefa[0]} ({tarefa[1]}) - Status: {tarefa[2]}")
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

dados = [
    ["Estudar Python", "Estudos", "Pendente"],
    ["Comprar leite", "Mercado", "Pendente"]
]
i = -1
while True:
    print("\n--==Lista de Tarefas==--")
    print(" [1]Adicionar Tarefa\n [2]Alterar Tarefa\n [3]Visualizar")
    acao = int(input("Ação: "))
    if acao == 1:
        adicionar()
        print("Dados Salvos Com Sucesso!")
    if acao == 2:
        alterar()
    if acao == 3:
        visualizar()



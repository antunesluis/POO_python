def pergunta_acao():
    print()
    print("comandos: listar, desfazer, refazer")
    return input("Digite uma tarefa ou comando: ")


def adiciona_tarefa(tarefa, lista_tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print("Voce não digitou nada!!!")
        return lista_tarefas

    lista_tarefas.append(tarefa)
    return lista_tarefas


def listar_tarefas(lista_tarefas):
    print()
    if not lista_tarefas:
        print("Nenhuma Tarefa para imprimir!!!")
        return

    print("TAREFAS:")
    for item in lista_tarefas:
        print(f'\t{item}')


def refaz_acao(lista_tarefas, itens_apagados):
    print()
    if not itens_apagados:
        print("Nada a Refazer!!!")
        return

    primeiro_removido = itens_apagados[-1]
    lista_tarefas.append(primeiro_removido)
    itens_apagados.pop(-1)

    listar_tarefas(lista_tarefas)


def desfaz_acao(lista_tarefas, itens_apagados):
    print()
    if not lista_tarefas:
        print("Nada a desfazer!!!")
        return

    removido = lista_tarefas.pop()
    itens_apagados.append(removido)

    listar_tarefas(lista_tarefas)


opcao_acao = pergunta_acao()
lista_tarefas = []
itens_apagados = []

while True:
    if opcao_acao == "listar":
        listar_tarefas(lista_tarefas)

    elif opcao_acao == "desfazer":
        desfaz_acao(lista_tarefas, itens_apagados)

    elif opcao_acao == "refazer":
        refaz_acao(lista_tarefas, itens_apagados)

    else:
        lista_tarefas = adiciona_tarefa(opcao_acao, lista_tarefas)

    opcao_acao = pergunta_acao()

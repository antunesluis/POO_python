def avalia_resposta(questao):
    print(questao['opcoes'])
    opcao = input()

    if opcao in str(questao['opcoes']):
        return True
    else:
        print('\nopcao invalida')
        return False


def realiza_pergunta(perguntas):
    pontos = 0
    for questao in perguntas:
        print(questao['pergunta'])
        print('\nDigite a opcao de acordo com a resposta correta:')

        if avalia_resposta(questao):
            pontos += 1

        print('-' * 50)

    return pontos


perguntas = [
    {
        'pergunta': 'Quanto é 2+5?',
        'opcoes': [3, 6, 7, 8, 10],
        'resposta': 7,
    },
    {
        'pergunta': 'Quanto é 10*5?',
        'opcoes': [14, 40, 50, 80, 100],
        'resposta': 50,
    },
    {
        'pergunta': 'Quanto é 30/5?',
        'opcoes': [5, 6, 7, 8, 10],
        'resposta': 6,
    },
]

# teste

pontos_finais = realiza_pergunta(perguntas)
print("Pontuação final:", pontos_finais)

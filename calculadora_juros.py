def juros_simples():
    valor_juros_simples = valor + (valor * porcentagem * tempo)
    print('Valor com juros simples: ', valor_juros_simples, 'Porcentagem: ', porcentagem)

def juros_composto():
    for momento in range(tempo+1):
        valor_juros_composto = valor * (1 + porcentagem) ** momento
        print('Mês: ', momento, 'Valor com juros composto: ', valor_juros_composto)

def operacao_abatimento():
    valor_final = valor - (valor * porcentagem * tempo)
    valor_abatimento = valor - valor_final
    print(f'{porcentagem * 100} % de {valor}: {valor_abatimento}. Valor menos {porcentagem * 100} %: {valor_final}')

while True:
    valor = int(input('Valor: '))
    porcentagem = int(input('Juros: ')) * 0.01
    tempo = int(input('Tempo: '))
    comando = input('Escolha operação:\nJuros Simples: 0, Juros Composto: 1, Calculadora Juli: 2.\n0, 1 ou 2? ')

    if comando == '0':
        juros_simples()
    elif comando == '1':
        juros_composto()
    elif comando == '2':
        operacao_abatimento()
    else:
        comando = input('Erro. Valor desconhecido.\nEscolha operação:\nJuros Simples: 0, Juros Composto: 1, Calculadora Juli: 2.\n0, 1 ou 2? ')

    reiniciar = input('Nova operação? Sim: 0, Não: 1.\n0 ou 1: ')
    if reiniciar == '1':
        break
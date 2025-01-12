import random
valor = {'A': 10,  '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10,'K':10}

def blackjack():
    while True:
        cartas = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q','K']
        jogador_1 = []
        maquina = []
        intro()
        primeira_rodada(cartas, jogador_1, maquina)
        segunda_rodada(cartas, jogador_1, maquina)
        final(cartas, jogador_1, maquina)
        if input('Nova partida: ').lower() == 'n':
            print('Até a próxima.')
            break
def intro():
    print('''
 >  BLAQ_JACK\n
    Regras:
    2 cartas suas contra 2 da máquina.
    O objetivo é estar mais próximo de {x} no TOTAL do que a máquina.
    Você tem direito a pedir uma nova carta enquanto não ultrapassar o TOTAL de {x}.
    Caso ultrapasse, você perdeu.
    Você vence automaticamente se atingir o TOTAL de {x}.
    Você empata se tiver o mesmo valor da máquina.
    Bom jogo !          
'''.format(x = 21))
def primeira_rodada(cartas, jogador_1, maquina):
    maquina.append(dar_carta(cartas))
    maquina.append(dar_carta(cartas))
    
    jogador_1.append(dar_carta(cartas))
    jogador_1.append(dar_carta(cartas))
    resultado(jogador_1, maquina)   
def segunda_rodada(cartas, jogador_1, maquina):
    while True:
        if input('Nova carta: ').lower() != 'n':
            jogador_1.append(dar_carta(cartas))
            print(f'Jogador_1: | {tratamento_cartas(jogador_1)} |')
            print(f'Pontuação: {contar_carta(jogador_1)}\n')
        else:
            break
    
    while True:
        if contar_carta(maquina) < 16 or contar_carta(maquina) < contar_carta(jogador_1) < 21:
            maquina.append(dar_carta(cartas))
            print(f'Máquina: | {tratamento_cartas(maquina)} |')
            print(f'Pontuação: {contar_carta(maquina)}\n')
        else:
            break
    resultado(jogador_1, maquina)
def dar_carta(cartas):
    id_carta = random.randrange(len(cartas))
    carta = cartas[id_carta]
    del(cartas[id_carta])
    return carta
def contar_carta(cartas_de_):
    conta = 0
    for carta in cartas_de_:
        conta += valor[carta]
    return conta
def resultado(jogador_1, maquina):
    print(f'\nMáquina: | {tratamento_cartas(maquina)} |')
    print(f'Pontuação: {contar_carta(maquina)}')
    print(f'Jogador_1: | {tratamento_cartas(jogador_1)} |')
    print(f'Pontuação: {contar_carta(jogador_1)}\n')
def final(cartas, jogador_1, maquina):
    print(f'Cartas restantes: | {tratamento_cartas(cartas)} |')
    if contar_carta(jogador_1) == 21 or 21 >= contar_carta(jogador_1) > contar_carta(maquina) or contar_carta(maquina) > 21:
        print('Venceu!')
    elif 21 > contar_carta(jogador_1) == contar_carta(maquina):
        print('Empate')
    else:
        print('Perdeu!')
def tratamento_cartas(cartas_de_):
    cartas_tratadas = ''
    for tratamento in str(cartas_de_):
        if tratamento == "'" or tratamento == "[" or tratamento == "]":
            tratamento = ''
        cartas_tratadas += tratamento
    cartas_tratadas = cartas_tratadas.replace(',', ' |')
    return cartas_tratadas

blackjack()
import random

def escolher_numero():
    return random.randrange(101)
def escolher_dificuldade():
    dificuldade = input('[F] ácil ou [D] ifícil ? ').lower()
    if dificuldade == 'f':
        chances = 10
    else:
        chances = 5
    return chances
def adivinhar_numero(numero, chances):
    print(numero)
    while True:
        if chances == 0:
            print('PERDEU\nFim de JOGO')
            break
        tentativa = int(input('Número: '))
        if tentativa == numero:
            print('ACERTOU')
            break
        elif tentativa > numero:
            chances -= 1
            print('MUITO')
            print(chances)
        elif tentativa < numero:
            chances -= 1
            print('POUCO')
            print(chances)
def jogar_novamente():
    while True:
        if input('Jogar Novamente: [s] ou [n] ? ').lower() != 'n':
            adivinhar_numero(numero = escolher_numero(), chances = escolher_dificuldade())
        else:
            print('Adeus!')
            break

adivinhar_numero(numero = escolher_numero(), chances = escolher_dificuldade())
jogar_novamente()
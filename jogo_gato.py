import random

# criação das listas
arbusto = '\U0001F333'
fila1 = [arbusto, arbusto, arbusto]
fila2 = [arbusto, arbusto, arbusto]
fila3 = [arbusto, arbusto, arbusto]

# visualização das listas
mapa = [fila1, fila2, fila3]
mapa_coluna = (f' 1| 2| 3 \n'+'|'.join(mapa[0]) + '\n' + '|'.join(mapa[1]) + '\n' + '|'.join(mapa[2]))
mapa_fila = (f'1|'+'|'.join(mapa[0]) + '\n2|' + '|'.join(mapa[1]) + '\n3|' + '|'.join(mapa[2]))

# jogo
fim = False
while not fim:

    # posicionamento do gato
    coluna = random.randint(0,2)
    fila = random.randint(0,2)
    
    # descobrir resultado
    print(f'RESULTADO: Coluna: {coluna + 1} Fila: {fila +1}')
    
    # apresentação do jogo
    print(f' - Desafio do Gato -\nEncontre o \U0001F638 entre os {arbusto}')
    mapa[fila][coluna] = '\U0001f63a'
    mapa_gato = '|'.join(mapa[0]) +'\n' + '|'.join(mapa[1]) + '\n' + '|'.join(mapa[2])
    vertical = int(input(f'\nEm que coluna está o gato?\n\n{mapa_coluna}\n\nResposta: ')) - 1
    horizontal = int(input(f'\nEm que fileira está o gato?\n\n{mapa_fila}\n\nResposta: ')) - 1
    
    # resultado
    if int(horizontal) == fila and int(vertical) == coluna:
        print(mapa_gato)
        print('\nVocê encontrou o \U0001f63a!')
        recomecar = input('\nGostaria de jogar novamente?\nS ou N: ')
        if recomecar == 'N':
            print('\nMuito obrigado!')
            fim = True
    else:
        continuar = input('\nO \U0001f63e fugiu! Gostaria de tentar novamente?\nS ou N: ')
        if continuar == 'N':
            print('\nMuito obrigado!')
            fim = True
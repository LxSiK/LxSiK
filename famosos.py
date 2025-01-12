from dados_famosos import dados
import random

def sortear_famoso():
    famoso = random.choice(dados)
    dados.remove(famoso)
    return famoso
def escolher_opcao(opcao_1,opcao_2):
    if input('Opção [A] ou [B]? ').lower() == 'a':
        escolha = opcao_1
    else:
        escolha = opcao_2
    return escolha
def comparar_seguidores(opcao_1, opcao_2, escolha):
    if opcao_1['seguidores'] > opcao_2['seguidores']:
        return opcao_1
    elif opcao_1['seguidores'] == opcao_2['seguidores']:
        return escolha
    else:
        return opcao_2
def jogo():
    while True:
        print('Jogo dos Famosos.\nEscolha quem tem o maior número de seguidores.')
        pontuacao = 0
        opcao_1 = sortear_famoso()

        while True:
            print(f'[A]: {opcao_1}')

            opcao_2 = sortear_famoso()
            print(f'[B]: {opcao_2}')

            escolha = escolher_opcao(opcao_1, opcao_2)

            if escolha == comparar_seguidores(opcao_1, opcao_2, escolha):
                pontuacao += 1
                opcao_1 = escolha
                print(f'Parabéns. Pontuação atual: {pontuacao}')
            else:
                print(f'Fim de jogo. Pontuação final: {pontuacao}')
                break
        
        if input('Continuar jogando: [S] ou [N] ').lower() == 'n':
            print('Volte sempre!')
            break

jogo()


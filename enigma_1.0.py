# escolher entre codificar ou decodificar a mensagem
def enigma():
    fim = False
    while not fim:
        comando = int(input('0 - Codificar\nou\n1 - Decodificar\n'))
        if comando == 0:
            codificar(mensagem_codificada)
            fim = True
        elif comando == 1:
            decodificar(mensagem_decodificada)
            fim = True
        else:
            print('Tente novamente.')

# cofificar a mensagem
def codificar(mensagem_codificada):

    # adicionar caracter inesperado
    for caracter_mensagem in mensagem:
        if caracter_mensagem not in alfabeto:
            mensagem_codificada += caracter_mensagem

        # posição e reposição de caracter
        posicao_caracter = 1
        for caracter_checado in alfabeto:
            if caracter_checado != caracter_mensagem:
                posicao_caracter += 1
            else:
                posicao_final_caracter = posicao_caracter + chave
                if posicao_final_caracter >= 25:
                    posicao_final_caracter -= 25
                mensagem_codificada += alfabeto[posicao_final_caracter - 1]
    print(f'Mensagem codificada: ', mensagem_codificada)

# decodificar a mensagem
def decodificar(mensagem_decodificada):

    # adicionar caracter inesperado
    for caracter_codificado in mensagem:
        if caracter_codificado not in alfabeto:
            mensagem_decodificada += caracter_codificado

        # posição e reposição de caracter
        posicao_caracter = 0
        for caracter_checado in alfabeto:
            if caracter_checado != caracter_codificado:
                posicao_caracter += 1
            else:
                posicao_final_caracter = posicao_caracter - chave
                mensagem_decodificada += alfabeto[posicao_final_caracter]
    print(f'Mensagem decodificada: {mensagem_decodificada}')

# valores dados
alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
mensagem_codificada = ''
mensagem_decodificada = ''

# input
mensagem = input('Mensagem: ').lower()
chave = int(input('Chave: '))
while chave >= 25 or chave < 1:
    chave = int(input('Chave entre 1 e 24.\nChave: '))

enigma()
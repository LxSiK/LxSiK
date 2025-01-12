def codificar(mensagem_codificada):

# adicionar caracter inesperado
    for caracter_mensagem in mensagem_decodificada:
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
    print(f'Mensagem_codificada: ', mensagem_codificada) 

# input
mensagem_decodificada = input('Mensagem: ').lower()
chave = int(input('Chave: '))
while chave >= 25 or chave < 1:
    chave = int(input('Chave entre 1 e 24.\nChave: '))

# valores dados
alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
mensagem_codificada = ''

codificar(mensagem_codificada)
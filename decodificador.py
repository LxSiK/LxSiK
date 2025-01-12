def decodificar(mensagem_decodificada):

# adicionar caracter inesperado
    for caracter_codificado in mensagem_codificada:
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

# input
mensagem_codificada = input('Mensagem: ').lower()
chave = int(input('Chave: '))
while chave >= 25 or chave < 1:
    chave = int(input('\nChave entre 1 e 24.\nChave: '))

# valores dados
alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
mensagem_decodificada = ''

decodificar(mensagem_decodificada)
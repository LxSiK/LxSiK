# valores dados
alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
caracter_escolhido = ''

# input
mensagem = input('Mensagem: ').lower()
chave = int(input('Chave: '))
while chave >= 25 or chave < 1:
    chave = int(input('Chave entre 1 e 24.\nChave: '))
comando = input('C - Codificar ou D- Decodificar: ').lower()
while comando != 'c' and comando != 'd':
    comando = input('Tente novamente.\nC - Codificar ou D- Decodificar: ')

# adicionar caracter inesperado
for caracter in mensagem:
    if caracter not in alfabeto:
        caracter_escolhido += caracter
    
    # posição de caracter 
    else:
        posicao_caracter = 0
        for caracter_checado in alfabeto:
            if caracter_checado != caracter:
                posicao_caracter += 1
            else:

                # codificar
                if  comando == 'c':
                    posicao_caracter_chaveado = posicao_caracter + chave
                    if posicao_caracter_chaveado >= 24:
                        posicao_caracter_chaveado -= 25
                
                # decodificar
                elif comando == 'd':
                    posicao_caracter_chaveado = posicao_caracter - chave
                caracter_escolhido += alfabeto[posicao_caracter_chaveado]
print(caracter_escolhido)
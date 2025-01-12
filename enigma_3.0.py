# iniciar
fim = False
while not fim:
    print('\n[ ENIGMA - a Máquina de Código ]\n')
    # inserção
    mensagem = input('Mensagem inserida: ').lower()
    chave = int(input('Chave: '))
    while chave >= 25 or chave < 1:
        chave = int(input('Chave entre 1 e 24.\nChave: '))
    comando = input('\nC - Codificar ou D- Decodificar: ').lower()
    while comando != 'c' and comando != 'd':
        comando = input('Tente novamente.\nC - Codificar ou D - Decodificar: ')

    # caracter inesperado
    alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
    caracter_escolhido = ''
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
                        resultado = 'Codificando...\n\nMensagem codificada: '
                        posicao_caracter_chaveado = posicao_caracter + chave
                        if posicao_caracter_chaveado >= 24:
                            posicao_caracter_chaveado -= 25
                    
                    # decodificar
                    elif comando == 'd':
                        resultado = '\nCodificando...\n\nMensagem decodificada: '
                        posicao_caracter_chaveado = posicao_caracter - chave
                    caracter_escolhido += alfabeto[posicao_caracter_chaveado]
    
    #resultado
    print(f'{resultado}{caracter_escolhido}\nChave: {chave}')
    
    # finalizar
    novo_comando = input('\nF - Fechar ou N - Novamente: ').lower()
    if novo_comando == 'f':
        print('Até logo!')
        fim = True
    else:
        print('Reiniciando...')
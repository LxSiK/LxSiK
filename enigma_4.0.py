def enigma():
   
    # iniciar programa
    fim = False
    while not fim:
        
        # inserção
        direcao = input("C - Codificar | D - Decodificar: ").lower()
        texto = input("Mensagem: ").lower()
        chave = int(input("Chave: ")) % 26
        
        # operação
        caesar(texto_inicial=texto, valor_chave=chave, direcao_chave=direcao)
        
        # fim do programa(?)
        reiniciar = input('Reiniciar? S ou N: ').lower()
        if reiniciar == 'n':
            print('Encerrando...')
            fim = True
        else:
            print('Reiniciando...\n')

def caesar(texto_inicial, valor_chave, direcao_chave):
    
    # valores dados
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    texto_final = ""
    
    # chave decodificador
    if direcao_chave == "d":
        valor_chave *= -1
    
    # tratamento caracteres inesperados
    for caracter in texto_inicial:
        if caracter not in alfabeto:
            texto_final += caracter
        
        # posicionamento chaveado
        else:
            posicao = alfabeto.index(caracter)
            nova_posicao = posicao + valor_chave
            
            # adição de caracter
            texto_final += alfabeto[nova_posicao]
    
    # resultado
    print(f"Mensagem: {texto_final}")

enigma()
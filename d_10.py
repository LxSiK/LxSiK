import random
while True:
    numero_dados = int(input('Número de dados: '))
    numero_sucessos = 0
    numero_falhas = 0
    for rolagem in range(numero_dados):
        resultado = random.randrange(0,10)
        if resultado >= 6 or resultado == 0:
            print(resultado, 'SUCESSO')
            numero_sucessos += 1 
        elif resultado == 1:
            numero_falhas += 1 
            print(resultado, 'FALHA')
        else:
            print(resultado)
    if numero_sucessos - numero_falhas >= 1:
        print(f"{'+'*20}\n{numero_sucessos - numero_falhas} sucesso(s).")
        #print('+'*20,'\n', numero_sucessos - numero_falhas, 'sucessos.')
    elif numero_falhas > numero_sucessos:
        print('+'*20,'\nFALHA CRíTICA.')
    else:
        print('+'*20,'\nFalha.')
    reiniciar = input('Nova rolagem?\n[s/n]:  ').lower()
    if reiniciar == 's':
        break
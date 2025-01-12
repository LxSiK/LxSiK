palavra = input('Insira uma palavra: ').lower()
print('\n'*100)
segredo = []
for _ in range(len(palavra)):
    segredo += '_'

forca = ['\U0001F480', '\U0001F635', '\U0001F922', '\U0001F912', '\U0001F974', '\U0001F603']
fim = False
erros = 5
palpite = []

print('\n', forca[erros], ' '.join(segredo), forca[erros])

while not fim:
    letra = input('\n> Insira uma letra: ').lower()
    
    while letra in palpite:
        print(f'='*20 ,'\n\n> Letra repetida','\nLetras usadas:' , ', '.join(palpite))
        letra = input('\n> Insira outra letra: ').lower()

    palpite += letra
    
    for posicao in range(len(palavra)):
        checagem = palavra[posicao]    
        if checagem == letra:
            segredo[posicao] = letra          

    if letra not in palavra:
        erros -= 1

    print(f'\n', forca[erros], ' '.join(segredo), forca[erros])
    print(f'='*20,'\n\nLetras usadas:',', '.join(palpite)) 
    
    if '_' not in segredo:
        fim = True
        print('\n', forca[erros], 'VOCÊ VENCEU!' + forca[erros])
    elif erros == 0:
        fim = True
        print('\n', forca[erros], 'VOCÊ PERDEU!' + forca[erros])
altura = int(input('Qual a sua altura em cm? '))
preco = 0

if altura >= 120:   
    
    idade = int(input('Qual a sua idade? '))
    
    if idade < 12:
        preco += 5
    elif idade <= 18:
        preco += 7
    else:
        preco += 12

    foto = input('Quer uma foto? [S / N] ')
    
    if foto == 'S':
        preco += 3
        
    print(f'Preço do ticket: ${preco}.')
else:
    print('Você não tem a altura requerida.')
numero = int(input('> Escolha um número entre 0 e 100: '))
while numero > 100:
    numero = int(input('\n🍺Beba!🍺\n\n> Escolha um número entre 0 e 100: '))

print('\n'*200)
fim = False
menor = 0
maior = 100

while not fim:
    tentativa = int(input(f'\n> Escolha um número entre {menor} e {maior}: '))
    if tentativa == numero:
        print('\nVocê acertou!')
        fim = True
    elif tentativa > numero and tentativa < maior:
        maior = tentativa
    elif tentativa < numero and tentativa > menor:
        menor = tentativa
    else:
        print('\n🍺Beba!🍺')
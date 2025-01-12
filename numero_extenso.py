numero_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    numero = int(input('Digite um número: '))
    if 0 <= numero <= 20:
        break
    print('Número entre 0 e 10.', end = ' ')
print(f'Número digitado: {numero_extenso[numero]}.')
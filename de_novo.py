lista = input('Qual a sua altura: ').split()

for n in range(0, len(lista)):
    lista[n] = int(lista[n])

maior = 0

for altura in lista:
    if altura > maior:
        maior = altura

print(maior)
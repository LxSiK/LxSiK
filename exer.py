'''
# comparar elementos em lista
lista = input('Lista de números: ').split()

for n in range(0, len(lista)):
    lista[n] = int(lista[n])

menor = lista[n]
maior = lista[n]
total = 0

for x in lista:
    if x < menor:
        menor = x

for y in lista:
    if y > maior:
        maior = y

for z in lista:
    total += z

print(menor)
print(maior)
print(total)
'''

'''
total2 = 0
for number in range (0, 101, 2):
    print(number)
    total2 += number

print(total2)
'''

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        number = 'FizzBuzz'
    elif number % 5 == 0:
        number = 'Buzz'
    elif number % 3 == 0:
        number = 'Fizz'
    print(number)
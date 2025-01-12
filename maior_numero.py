import random
cinco_numeros = (random.randrange(100),random.randrange(100),random.randrange(100),random.randrange(100),random.randrange(100))
for numeros in cinco_numeros:
    print(numeros, end=' ')
cinco_numeros = sorted(cinco_numeros)
print(f'\n{cinco_numeros[0]}, {cinco_numeros[4]}')
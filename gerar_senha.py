import random
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Gerador de Senhas')
nr_letras = int(input('Quantidade de letras: '))
nr_numeros = int(input('Quantidade de números: '))
nr_simbolos = int(input('Quantidade de simbolos: '))

senha_letras = ''
for x in range(0, nr_letras):
    x = random.choice(letras)
    senha_letras += x

senha_numeros = ''
for y in range(0, nr_numeros):
    y = random.choice(numeros)
    senha_numeros += y

senha_simbolos = ''
for z in range(0, nr_simbolos):
    z = random.choice(simbolos)
    senha_simbolos += z

senha = senha_letras + senha_numeros + senha_simbolos
print(('').join(random.sample(senha,len(senha))))
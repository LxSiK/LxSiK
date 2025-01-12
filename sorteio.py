import random
nomes = input('Nomes: ')
lista_de_nomes = nomes.split()
escolha = random.randint(0, len(lista_de_nomes) - 1)
print(lista_de_nomes[escolha])
print(', '.join(lista_de_nomes))
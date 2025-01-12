import math

def numero_primo(numero):
    sim = f"{numero} é número primo."
    nao = f"{numero} não é número primo."
    raiz_de_numero = int(math.sqrt(numero))
    primo = True
    
    if 0 < numero < 3:
        valor = sim
    for x in range(2,raiz_de_numero + 1):
        if numero % x == 0:
            primo = False
    if primo == True:
        valor = sim
    else:
        valor = nao
    print(valor)

numero = int(input("Adicione um número: "))
numero_primo(numero)
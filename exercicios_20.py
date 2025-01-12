# 99 checagem valores em lista

def comparacao(lista_numeros):
    for numero in lista_numeros:
        for maior_numero in lista_numeros:
            if numero < maior_numero:
                numero = maior_numero
        numero_maior = numero
        for menor_numero in lista_numeros:
            if numero > menor_numero:
                numero = menor_numero
        numero_menor = numero
    print('Maior número:',numero_maior, 'Menor número:', numero_menor)

fim_checagem = False
lista_numeros = []

while not fim_checagem:
    numero = int(input('Valor: '))
    lista_numeros += [numero]
    adicionar_numero = input('Adicionar novo número [s / n]: ')
    if adicionar_numero == 'n':
        fim_checagem = True

comparacao(lista_numeros)

'''
# 98 - contagem personalizada
def contagem(numero_atual, passo):
    lista_numeros = []
    lista_numeros_inversos = []
    while numero_atual <= numero_final:
        lista_numeros += [numero_atual]
        numero_atual += passo
    
    lista_numeros_inversos += reversed(lista_numeros)
    
    if reverso:
        print(lista_numeros_inversos)
    else:
        print(lista_numeros)

numero_inicial = int(input('Número inicial: '))
numero_final = int(input('Número final: '))

if numero_inicial > numero_final:
    numero_atual = numero_final
    numero_final = numero_inicial
    reverso = True
else:
    numero_atual = numero_inicial
    reverso = False

passo = int(input('Passo: '))
if passo < 0:
    passo *= (-1)    
elif passo == 0:
    passo = 1

contagem(numero_atual, passo)


# 97 - decorar mensagem
def decorar(lista_mensagens):
    numero_mensagens = 0
    for mensagens in lista_mensagens:
        numero_mensagens += 1
        for mensagem in lista_mensagens:
            mensagem = lista_mensagens[numero_mensagens-1]
            numero_caracteres = 0
            for caracteres in mensagem:
                numero_caracteres += 1 
        print('='*numero_caracteres, '\n' + mensagem, '\n' + '=' * numero_caracteres)

fim = False
lista_mensagens = []
while not fim:
    lista_mensagens += [input('Insira mensagem: ')]
    comando = input('Inserir nova mensagem [s/n]: ').lower()
    if comando == 'n':
        fim = True    
decorar(lista_mensagens)


# 96 - calcular área
def calcular_area(largura, comprimento):
    area = largura * comprimento
    print(f'Área: {area} m²')

largura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))
calcular_area(largura, comprimento)
'''

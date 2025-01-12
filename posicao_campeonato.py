time = input('Time: ')
times = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense', 'Athleticco-PR', 'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América-MG')
lista_quatro_primeiros = []
lista_quatro_ultimos = []
pos = 1
for quatro_primeiros in times[0:4]:
    lista_quatro_primeiros += [quatro_primeiros]
for quatro_ultimos in times[16:20]:
    lista_quatro_ultimos += [quatro_ultimos]
for colocacao in times:
    colocacao = colocacao.lower()
    if colocacao == time.lower():
        pos_final = pos
    else:
        pos += 1
lista_quatro_primeiros = ', '.join(lista_quatro_primeiros)
lista_quatro_ultimos = ', '.join(lista_quatro_ultimos)
print(f'Quatro primeiros colocados: {lista_quatro_primeiros}.')
print(f'Quatro últimos colocados: {lista_quatro_ultimos}.')
print(f'{time} está em {pos_final}º.')
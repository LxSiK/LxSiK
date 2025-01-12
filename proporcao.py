caminhar = int(input('caminhada: '))
correr = int(input('corrida: '))
exercicio_total = caminhar + correr 
semana_atual = 1
print('Semana: ',semana_atual, 'Corrida: ', correr, 'km', 'Caminhada: ', caminhar, 'km.')
while correr != exercicio_total:
        semana_atual += 1
        correr = correr + 0.25
        caminhar -= 0.25
        print('Semana: ',semana_atual, 'Corrida: ', correr, 'km', 'Caminhada: ', caminhar, 'km.')
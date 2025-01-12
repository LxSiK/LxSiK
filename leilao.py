def lance():
    registro = []
    maior_lance = rodada = 0

    while True:
        nome = str(input('Nome: '))
        valor_lance = int(input('Lance: $'))
        lance = {
                'Nome' : nome, 
                'Lance' : valor_lance,
                }
        
        if valor_lance > maior_lance:
            maior_lance = valor_lance
            rodada_vencedora = rodada
        
        registro.append(lance)

        adicionar = input('Adicionar novo lance? [s/n]: ').lower()
        if adicionar == 'n':
            print(registro)
            print('Vencedora:', registro[rodada_vencedora]['Nome'], '\nRemate: $', registro[rodada_vencedora]['Lance'])
            break
        rodada += 1

lance()
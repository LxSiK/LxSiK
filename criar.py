def Insercao():
    switch = True
    while switch == True:
        user = input('Função de inserção de dados: \nSim [s] ou Não [n]: ')
        if user == 's':
            dados_nome = input('Nome: ')
            dados_cpf = input('CPF: ')
            dados_endereco = input('Endereço: ')
            lista_dados = [dados_nome, dados_cpf, dados_endereco]
            print(f'Nome: {lista_dados[0]}\nCPF: {lista_dados[1]}\nEndereço: {lista_dados[2]}')
            user = input('Confirma? Sim [s] ou Não [n]: ')
            if user == 's':
                print('Obrigado!')
            elif user == 'n':
                modificar = input('Modificar:\nNome: [n]\nCPF: [c]\nEndereço:[e]\n')
                if modificar == 'n':
                    lista_dados[0] = input('Novo Nome: ')
                elif modificar == 'c':
                    lista_dados[1] = input('Novo CPF: ')
                elif modificar == 'e':
                    lista_dados[2] = input('Novo Endereço: ')
                print(f'Nome: {lista_dados[0]}.\nCPF: {lista_dados[1]}\nEndereço: {lista_dados[2]}')
        elif user == 'n':
            switch = False
        else:
            user = input('Tente novamente.\nClique em qualquer tecla.')

Insercao()
import time

# constantes
CAFES = {
    'Espresso': {
        'ingredientes': {
            'água': 50,
            'café': 10,
            'leite': 0,
        },
        'custo': 1.50,
    },
    'Latte': {
        'ingredientes': {
            'água': 200,
            'café': 24,
            'leite': 150,
        },
        'custo': 2.50,
    },
    'Cappuccino': {
        'ingredientes': {
            'água': 250,
            'café': 24,
            'leite': 100,
        },
        'custo': 3.00,
    }
}

PRECO_RECARGA = {
     'água': 0.1,
     'café': 0.5,
     'leite': 0.2,
}

RECURSOS_MAXIMO = {
     'água': 500,
     'café': 250,
     'leite': 300,
}

OPCOES = {
     '1' : 'Espresso',
     '2' : 'Latte',
     '3' : 'Cappuccino',
     'R' : 'Recarga',
     'M' : 'Manual',
     '0' : 'Reiniciar',
     '00': 'Desligar',
     'X' : 'Desconhecida',
    }

MOEDAS = {
     '1': 0.1,
     '2': 0.25,
     '3': 0.5,
     '4': 1,
     '5': 2,
     }



# variantes
recursos = {
     'água': 300,
     'café': 100,
     'leite': 200,
     'caixa': 100
}



# funções do programa
def apresenta_opcoes():
    return print('''\U0001F916                  makn_d_kaf\n\n> Escolha uma opção:
                    [1]: Espresso
                    [2]: Latte
                    [3]: Cappuccino
                    [R]: Recarga
                    [M]: Manual''')


def atualiza_recursos(cafe_infos):
    recursos['caixa'] += cafe_infos['custo']
    recursos['água'] -= cafe_infos['ingredientes']['água']
    recursos['café'] -= cafe_infos['ingredientes']['café']
    recursos['leite'] -= cafe_infos['ingredientes']['leite']

    return recursos


def cafe_(opcao):
    cafe_infos = infos_cafe_(opcao)

    if recursos_suficientes(cafe_infos) == True:
    
        cafe_infos['pago'] = insere_moedas(cafe_infos)
        
        if cafe_infos['pago'] < cafe_infos['custo']:
            return print(f'''> Fundo insuficiente\n''')
        
        else:
            cafe_infos['troco'] = cafe_infos['pago'] - cafe_infos['custo']  

            recursos = atualiza_recursos(cafe_infos)

            print(f'''> {cafe_infos['nome']}: PRONTO ''')
            print(f'''> Troco: ${cafe_infos['troco']}\n''')
            return recursos
    
    else:
        return print(f'''> Info: 
                    [{opcao}]: {cafe_infos['nome']} indisponível
                         - É necessário recarregar os recursos\n''')


def confirma_(opcao, opcao_):
    print('\n'*50)
    print(f'''> Opção selecionada: 
                    [{opcao}]: {opcao_}''')
    
    if opcao_ == 'Espresso' or opcao_ == 'Latte' or opcao_ == 'Cappuccino':
        cafe_infos = infos_cafe_(opcao)
        print(f'''                         - Custo: ${cafe_infos['custo']}
                         - Ingredientes: Água: {cafe_infos['ingredientes']['água']} ml | Leite: {cafe_infos['ingredientes']['leite']} ml | Café: {cafe_infos['ingredientes']['café']} g''')
    
    elif opcao_ == 'Recarga':
        exibe_recursos()

    print(f'''                    [0]: Cancela''')

    if input('''> Confirma? ''') == '0':
        print(f'''                    [0]: Opção cancelada''')
        time.sleep(1)
        print('\n'*50)
        return False
    else:
        print(f'''                    [{opcao}]: Opção confirmada''')
        time.sleep(1)
        print('\n'*50)
        return True


def infos_cafe_(opcao):
    cafe_infos = {}
    cafe_infos['nome'] = OPCOES[opcao]
    cafe_infos['ingredientes'] = CAFES[cafe_infos['nome']]['ingredientes']
    cafe_infos['custo'] = CAFES[cafe_infos['nome']]['custo']
    return cafe_infos


def insere_moedas(cafe_infos):
    valor_pago = 0
    
    while True:
        if valor_pago >= cafe_infos['custo']:
            break
        else:
            custo_restante = round(cafe_infos['custo'] - valor_pago, 3)
            print(f'''> Custo restante:   ${custo_restante}''')
        
        print('''> Insira moedas:
                    [1]: 10 centavos
                    [2]: 25 centavos
                    [3]: 50 centavos
                    [4]: 1 real
                    [5]: 2 reais
                    [0]: Encerra''')
        moeda = input(f'''> Digite aqui: ''')

        if moeda == '0':
            if input('''> Confirma? ''') != '0':
                print('\n'*50)
                break
        elif moeda not in MOEDAS:
            print('> Moeda desconhecida\n> Tente novamente')
            time.sleep(2)
        else:
            valor_pago += MOEDAS[moeda]
            print(f'''> Valor adicionado: ${valor_pago}''')
            time.sleep(2)
            print('\n'*50)

    return valor_pago


def intro():
    #print('\U0001F916 \U00002615 MAQUINA_DE_CAFÉ \U00002615 \U0001F916')
    print('\n'*50)
    assinatura = 'by LaS Sik'

    escrita = ''
    for p in assinatura:
        escrita += p
        print(escrita)
        time.sleep(0.3)
        print('\n' * 50)


    escrita = ''
    for q in range(0, len(assinatura) + 1):
        escrita = assinatura[q:10]
        print(escrita)
        time.sleep(0.2)
        print('\n' * 50)
            

def exibe_manual(): 
    return print(f'''> Manual: 
                    Digite [1] para café espresso - [Água: {CAFES['Espresso']['ingredientes']['água']} ml, Leite: {CAFES['Espresso']['ingredientes']['leite']} ml, Café: {CAFES['Espresso']['ingredientes']['café']} g]
                    Digite [2] para café latte - [Água: {CAFES['Latte']['ingredientes']['água']} ml, Leite: {CAFES['Latte']['ingredientes']['leite']} ml, Café: {CAFES['Latte']['ingredientes']['café']} g]
                    Digite [3] para café cappuccino - [Água: {CAFES['Cappuccino']['ingredientes']['água']} ml, Leite: {CAFES['Cappuccino']['ingredientes']['leite']} ml, Café: {CAFES['Cappuccino']['ingredientes']['café']} g]
                    Digite [R] para recarga de máquina
                    Digite [M] para ler manual
                    Digite [0] para reiniciar a máquina\n''')


def exibe_recursos():
    print(f'''                         - Caixa: ${recursos['caixa']}
                         - Ingredientes: Água: {recursos['água']} ml | Leite: {recursos['leite']} ml | Café: {recursos['café']} g''')
    

def realiza_(opcao, opcao_):
    if opcao_ == 'Espresso' or opcao_ == 'Latte' or opcao_ == 'Cappuccino':
        cafe_(opcao)
    elif opcao_ == 'Recarga':
        print('''> Recarga: ''')
        recarrega_recursos()
    elif opcao_ == 'Manual':
        exibe_manual()
    elif opcao_ == 'Reiniciar':
        print('> Reiniciando a Máquina em 2 segundos')
        time.sleep(2)
        print('\n'*50)
        intro()
        return 
    elif opcao_ == 'Desconhecida':
        print('''> Opção desconhecida\n> Tente novamente''')
    

def recarrega_recursos():
    recursos_necessarios = {
        'água': RECURSOS_MAXIMO['água'] - recursos['água'],
        'café': RECURSOS_MAXIMO['café'] - recursos['café'],
        'leite': RECURSOS_MAXIMO['leite'] - recursos['leite'],
        }
    
    while recursos['caixa'] > 1:
        for recurso in recursos_necessarios:
            if recursos_necessarios[recurso]:
                recursos[recurso] += 1
                recursos_necessarios[recurso] -= 1
                recursos['caixa'] -= PRECO_RECARGA[recurso]
                recursos['caixa'] = round(recursos['caixa'], 3)
        
    recursos['caixa'] = round(recursos['caixa'])
    exibe_recursos()
    return recursos


def recursos_suficientes(cafe_infos):
    recursos_info = []
    for recurso in recursos:
        for ingrediente in cafe_infos['ingredientes']:
            if ingrediente == recurso:
                if recursos[recurso] < cafe_infos['ingredientes'][ingrediente]:
                    recursos_info += [False]
                else:
                    recursos_info += [True]
    
    if False not in recursos_info:
        return True
    else:
        return False


def retorna_opcao():
    opcao = input('> Digite aqui: ').upper() 
    if opcao not in OPCOES:
        opcao = 'X'
    return opcao


def retorno_menu():
    input(f'''> Retornar ao MENU? ''')
    print('\n'*50)


# programa
intro()

while True:
    apresenta_opcoes()
    opcao = retorna_opcao()
    opcao_ = OPCOES[opcao]
    
    
    if confirma_(opcao, opcao_) == True:
        if opcao_ != 'Desligar': 
            realiza_(opcao, opcao_)
            retorno_menu()
        else:
            break
import time

# constantes
MENU = {
    'espresso': {
        'ingredientes': {
            'água': 50,
            'café': 10,
            'leite': 0,
        },
        'custo': 1.50,
    },
    'latte': {
        'ingredientes': {
            'água': 200,
            'café': 24,
            'leite': 150,
        },
        'custo': 2.50,
    },
    'cappuccino': {
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



# variantes
recursos = {
     'água': 300,
     'café': 100,
     'leite': 200,
     'caixa': 100,
}



# funções do programa
def intro():
    mensagens = ['\U0001F916 \U00002615 MAQUINA_DE_CAFÉ \U00002615 \U0001F916', '> Esquentando a máquina', '> Checando os recursos', '> Preparando as opções', '> Pronto para uso']
    for mensagem in mensagens:
        print(mensagem)
        #time.sleep(1)


def opcoes():
    return print('''> Escolha uma opção:
                [1]: Espresso
                [2]: Latte
                [3]: Cappuccino
                [R]: Recursos
                [M]: Manual''')


def escolha():
    return input('> Digite aqui: ').lower()


def opcao_recursos():
    return print(f'''> Recursos:
                Água:  {recursos['água']} ml
                Café:  {recursos['café']} g
                Leite: {recursos['leite']} ml\n''')


def opcao_manual(): 
    return print(f'''> Manual: 
                Digite [1] para café espresso - [Água: {MENU['espresso']['ingredientes']['água']} ml, Leite: {MENU['espresso']['ingredientes']['leite']} ml, Café: {MENU['espresso']['ingredientes']['café']} g]
                Digite [2] para café latte - [Água: {MENU['latte']['ingredientes']['água']} ml, Leite: {MENU['latte']['ingredientes']['leite']} ml, Café: {MENU['latte']['ingredientes']['café']} g]
                Digite [3] para café cappuccino - [Água: {MENU['cappuccino']['ingredientes']['água']} ml, Leite: {MENU['cappuccino']['ingredientes']['leite']} ml, Café: {MENU['cappuccino']['ingredientes']['café']} g]
                Digite [R] para status da máquina
                Digite [M] para ler manual
                Digite [0] para reiniciar a máquina\n''')


def cobranca(total, moeda, valor, opcao):
    total += moeda * valor
    total = round(total, 3)
    print(f'''> Valor depositado: $ {total}''')
    print(f'''> Custo restante: $ {(total - MENU[opcao]['custo']  * -1)}''')
    return total


def checagem_total(total, opcao):
    if total >= MENU[opcao]['custo']:
        return False


def cobrar_moedas(opcao):
    while True:
        total = 0
        print(f'''> Custo total: $ {MENU[opcao]['custo']}''')
        print('''> Insira as moedas: ''')

        dez = int(input('''
                - 10 centavos: '''))
        total = cobranca(total, dez, 0.1, opcao)
        if checagem_total(total, opcao) == False:
            break
        
        vinte_cinco = int(input('''
                - 25 centavos: '''))
        total = cobranca(total, vinte_cinco, 0.25, opcao)
        if checagem_total(total, opcao) == False:
            break

        cinquenta = int(input('''
                - 50 centavos: '''))
        total = cobranca(total, cinquenta, 0.5, opcao)
        if checagem_total(total, opcao) == False:
            break

        um = int(input('''
                - 1 real: '''))
        total = cobranca(total, um, 1, opcao)
        if checagem_total(total, opcao) == False:
            break

        dois = int(input('''
                - 2 reais: '''))
        total = cobranca(total, dois, 2, opcao)
        

    if total >= MENU[opcao]['custo']:
        print(f'''> Preparando café {MENU[opcao]}.''')
        troco = round(MENU[opcao]['custo'] - total, 2) * -1
        print(f'''Troco: ${troco} .''')
        recursos['caixa'] -= troco
        print(recursos['caixa'])
        return True
    else:
        print('> Moedas insuficientes')
        return False


def opcao_(opcao):
    if opcao == '1':
        opcao = 'espresso'
    elif opcao == '2':
        opcao = 'latte'
    elif opcao == '3':
        opcao = 'cappuccino'
    else:
        return print('> Opção inexistente. Tente novamente.')

    if cobrar_moedas(opcao) == True:

        if recursos['água'] >= MENU[opcao]['ingredientes']['água'] and recursos['leite'] >= MENU[opcao]['ingredientes']['leite'] and  recursos['café'] >= MENU[opcao]['ingredientes']['café']:
            recursos['água'] -= MENU[opcao]['ingredientes']['água']
            recursos['leite'] -= MENU[opcao]['ingredientes']['leite']
            recursos['café'] -= MENU[opcao]['ingredientes']['café']
            recursos['caixa'] += MENU[opcao]['custo']
            return print(recursos)
        else:
            return print('> Recursos insuficientes. Realize a recarga.')


def retorno_opcoes():
    input('> Retornar ao MENU OPÇÕES?\n')
    

def recarga_recursos(recursos):
    quantia_necessaria = {
        'água': RECURSOS_MAXIMO['água'] - recursos['água'], 
        'café': RECURSOS_MAXIMO['café'] - recursos['café'],
        'leite': RECURSOS_MAXIMO['leite'] - recursos['leite'],
        }
    
    if recursos['caixa'] == 0:
        print('> Recursos insuficientes')
    
    while recursos['caixa'] > 0:
        if quantia_necessaria['água'] > 0:
            recursos['água'] += 1
            quantia_necessaria['água'] -= 1
            recursos['caixa'] -= PRECO_RECARGA['água']

        elif quantia_necessaria['café'] > 0:
            recursos['café'] += 1
            quantia_necessaria['café'] -= 1
            recursos['caixa'] -= PRECO_RECARGA['café']
            
        elif quantia_necessaria['leite'] > 0:
            recursos['leite'] += 1
            quantia_necessaria['leite'] -= 1
            recursos['caixa'] -= PRECO_RECARGA['leite']
        else:
            break
    
    recursos['caixa'] = round(recursos['caixa'])
    print(f'''> Caixa: $ {recursos['caixa']}''')



# programa
intro()
while True:   
    opcoes()
    opcao = escolha()
    if opcao == 'r':
        opcao_recursos()
        print('''> Realizar recarga?
            [0]: Sim
            [1]: Não''')
        if input('''> Digite aqui: ''').lower() == '0':
            recarga_recursos(recursos)
            opcao_recursos()
        retorno_opcoes()
    elif opcao == 'm':
        opcao_manual()
        retorno_opcoes()
    elif opcao == '0':
        print('> Reiniciando a Máquina em 2 segundos')
        time.sleep(2)
        print('\n'*50)
        intro()
    elif opcao == '00':
        print('> Desligando a Máquina em 2 segundos')
        time.sleep(2)
        break       
    else:
        opcao_(opcao)
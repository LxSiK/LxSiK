MENU = {
    'espresso': {
        'ingredientes': {
            'água': 50,
            'café': 10,
            'leite': 0,
        },
        'custo': 1.5,
    },
    'latte': {
        'ingredientes': {
            'água': 200,
            'café': 24,
            'leite': 150,
        },
        'custo': 2.5,
    },
    'cappuccino': {
        'ingredientes': {
            'água': 250,
            'café': 24,
            'leite': 100,
        },
        'custo': 3.0,
    }
}

PRECO_RECARGA = {
     'água': 0.1,
     'café': 0.5,
     'leite': 0.2,
}

recursos = {
     'água': 300,
     'café': 100,
     'leite': 200,
     'caixa': 100,
}


def intro():
    print(f'''
\U0001F916 \U00002615 MAQUINA_DE_CAFÉ \U00002615 \U0001F916\n
> Iniciando ...
> Hmm... É hora do café!
> Escolha uma opção:
    [1]: Espresso
    [2]: Latte
    [3]: Cappuccino
    [0]: Recursos''')


def checagem_maquina(recursos):
    for recurso in recursos:
        print(recursos[recurso])
       

def retornar_pedido():
    pedido = input('> Insira aqui: ')
    if pedido == '0':
        return 'espresso'
    elif pedido == '1':
        return 'latte'
    elif pedido == '2':
        return 'cappuccino'


def cobrar_valor(recursos):
    pedido = retornar_pedido()
    print('####################')
    print(f'Pedido: {pedido.capitalize()}')
    print(f"Custo: {MENU[pedido]['custo']}")
    recursos['água'] -= MENU[pedido]['ingredientes']['água']
    recursos['café'] -= MENU[pedido]['ingredientes']['café']
    recursos['leite'] -= MENU[pedido]['ingredientes']['leite']
    recursos['caixa'] += MENU[pedido]['custo']
    print(recursos)
    return(recursos)



        





intro()
#recursos = cobrar_valor(recursos)

import random
fim = False

while not fim:
    y = random.randint(0,1)
    x = input('- Preciso saber se um dia irei ')
    
    if y == 0:
        print(f'- Sim, um dia você irá {x}')
    else:
        print(f'- Não, você nunca irá {x}')

    a = input('- Mais alguma pergunta?\n- ').lower()
    
    if a != 'sim':
        print('- Você teve sua resposta.')
        fim = True
import random
cartas = ['A', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q','K']
valor = {'A': 10,  1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 'J':10, 'Q':10,'K':10}


def blackjack():
    intro()

    machine_picks = initial_machine_picks()
    machine_score = initial_machine_score(machine_picks)
    print(f'Machine  Score\n| {machine_picks[0]} | {machine_picks[1]} | {machine_score}')

    user_picks = initial_user_picks()
    user_score = initial_user_score(user_picks)
    print(f'User     Score\n| {user_picks[0]} | {user_picks[1]} | {user_score}')
    
    new_user_score = new_user_pick(user_score, user_picks)
    
    
    
    new_machine_score = new_machine_pick(machine_score, machine_picks)



    
    

    
    

    
    
    
    
    
    
    
    
    
    
def intro():
    print('''
 * BlAQ_JAcK\n
    Regras:
    2 cartas suas contra 2 da máquina.
    O objetivo é estar mais próximo de {x} no TOTAL do que a máquina.
    Você tem direito a pedir uma nova carta enquanto não ultrapassar o TOTAL de {x}.
    Caso ultrapasse, você perdeu.
    Você vence automaticamente se atingir o TOTAL de {x}.
    Você empata se tiver o mesmo valor da máquina.
    Bom jogo !          
'''.format(x = 21))
        
def initial_machine_picks():
     machine_pick_1 = machine_pick()
     machine_pick_2 = machine_pick()
     machine_picks = [machine_pick_1, machine_pick_2]
     return machine_picks
def machine_pick():
    pick_id = random.randrange(len(cartas))
    machine_pick = cartas[pick_id]
    del(cartas[pick_id])
    return machine_pick
def initial_machine_score(machine_picks):
    return valor[machine_picks[0]] + valor[machine_picks[1]]

def initial_user_picks():
     user_pick_1 = user_pick()
     user_pick_2 = user_pick()
     user_picks = [user_pick_1, user_pick_2]
     return user_picks 
def user_pick(): 
        pick_id = random.randrange(len(cartas))
        user_pick = cartas[pick_id]
        del(cartas[pick_id])
        return user_pick
def initial_user_score(user_picks):
    return valor[user_picks[0]] + valor[user_picks[1]]

def new_user_pick(user_score, user_picks):
    while True:
        if input('Continuar: ').lower() != 'n':
            new_pick = user_pick()
            user_picks.append(new_pick)
            
            new_score = user_score + valor[new_pick]
            user_score = new_score
            
            result_user(user_picks, new_score)
        else:
            return user_score
def new_machine_pick(machine_score, machine_picks):
    while True:
        if machine_score < 16:
            new_pick = machine_pick()
            machine_picks.append(new_pick)

            new_score = machine_score + valor[new_pick]
            machine_score = new_score
            
            result_machine(machine_picks, new_score)
        else:
            return machine_score

def result_machine(machine_picks, machine_score):
    cards = ''
    for element in str(machine_picks):
        cards += element
    cards = cards[1:len(cards)-1].replace(',', ' |')
    cards = cards.replace("'",'')
    space = ' '*(len(cards)-3)
    return print(f'Machine{space}Score\n| {cards} | {machine_score}')
def result_user(user_picks, user_score):
    cards = ''
    for element in str(user_picks):
        cards += element
    cards = cards[1:len(cards)-1].replace(',', ' |')
    cards = cards.replace("'",'')
    space = ' '*(len(cards)-3)
    return print(f'User   {space}Score\n| {cards} | {user_score}')

def result(user_score, machine_score):
    while True:
        if machine_score > 21:
            result = 'Win !'
            break
        elif user_score > machine_score:
            result = 'Win !!'
            break
        elif machine_score > user_score:
            result = 'Lose !'
            break
        elif machine_score == user_score:
            result = 'Draw!'
            break
    return print(result)

blackjack()
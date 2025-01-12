import random
cartas = ['A', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q','K']

def blackjack():
    user_hand()
    machine_hand()

def user_hand():
    pick_user_1 = random.randrange(len(cartas))
    user_hand_1 = cartas[pick_user_1]
    del(cartas[pick_user_1])

    pick_user_2 = random.randrange(len(cartas))
    user_hand_2 = cartas[pick_user_2]
    del(cartas[pick_user_2])

    print(f'User hand\n| {user_hand_1} | {user_hand_2} |')

def machine_hand():
    pick_machine_1 = random.randrange(len(cartas))
    machine_hand_1 = cartas[pick_machine_1]
    del(cartas[pick_machine_1])

    pick_machine_2 = random.randrange(len(cartas))
    machine_hand_2 = cartas[pick_machine_2]
    del(cartas[pick_machine_2])
    print(f'Machine hand\n| {machine_hand_1} | {machine_hand_2} |')

blackjack()
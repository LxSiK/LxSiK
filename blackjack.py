import random
cartas = ['A', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q','K']

pick_user_1 = random.randrange(len(cartas))
user_hand_1 = cartas[pick_user_1]
del(cartas[pick_user_1])

pick_user_2 = random.randrange(len(cartas))
user_hand_2 = cartas[pick_user_2]
del(cartas[pick_user_2])

pick_machine_1 = random.randrange(len(cartas))
machine_hand_1 = cartas[pick_machine_1]
del(cartas[pick_machine_1])

pick_machine_2 = random.randrange(len(cartas))
machine_hand_2 = cartas[pick_machine_2]
del(cartas[pick_machine_2])

print('User hand:', user_hand_1, user_hand_2)
print('Machine hand:' ,machine_hand_1,machine_hand_2)
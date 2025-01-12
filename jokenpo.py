pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

lista = [pedra, papel, tesoura]
robo = random.randint(0,2)
mao = int(input('[0] Pedra\n[1] Papel\n[2] Tesoura\n0, 1 ou 2: '))

while mao > 2:
    print('Opção inválida.\nTente novamente:')
    mao = int(input('[0] Pedra\n[1] Papel\n[2] Tesoura\n0, 1 ou 2: '))

opc_mao = lista[mao]
opc_robo = lista[robo]

print(f'Você escolheu: {opc_mao}')
print(f'O oponente escolheu: {opc_robo}')

if mao == robo:
    print('Empate.')
elif mao == 2 and robo == 0:
    print('Você perdeu.')
elif mao == 0 and robo == 2:
    print('Você venceu!')
elif  robo > mao:
    print('Você perdeu.')    
elif mao > robo: 
    print('Você venceu!')


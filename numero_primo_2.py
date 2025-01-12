def checagem(numero):
  resposta = ['número primo.', 'número não primo.']
  x = 0
  for numeros in range(2, numero):
    if numero % numeros == 0:
      x = 1
  print(f'{numero} é {resposta[x]}')

n = int(input())
checagem(numero=n)
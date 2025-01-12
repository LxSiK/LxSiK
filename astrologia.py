erro = 'Data inválida.'
msg = 'Seu signo é'

# o ano deve ser divisível por 4, mas não por 100. Exceto quando pode é divisível por 400.
ano = int(input('Ano: '))
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    anobi = True
else:
    anobi = False

# verificação para mês.
mes = int(input('Mês: '))
while mes == 0 or mes > 12:
    mes = int(input(f'{erro}\nMês: '))

# verificação para dia baseado em mês e ano bissexto.
dia = int(input('Dia: '))
if anobi == True:
    while (mes == 2 and dia > 29) or (mes == 4 and dia > 30) or (mes == 6 and dia > 30) or (mes == 9 and dia > 30) or (mes == 11 and dia > 30) or dia > 31:
        dia = int(input(f'{erro}\nDia: '))
else:
    while (mes == 2 and dia > 28) or (mes == 4 and dia > 30) or (mes == 6 and dia > 30) or (mes == 9 and dia > 30) or (mes == 11 and dia > 30) or dia > 31:
        dia = int(input(f'{erro}\nDia: '))

# classificação do signo
if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        print(msg , 'Áries.')
elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        print(msg, 'Touro.')
elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 21):
        print(msg, 'Gêmeos.')
elif (mes == 6 and dia >= 22) or (mes == 7 and dia <= 22):
        print(msg, 'Câncer.')
elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        print(msg, 'Leão.')
elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        print(msg, 'Virgem.')
elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        print(msg, 'Libra.')
elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        print(msg, 'Escorpião.')
elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        print(msg, 'Sagitário.')
elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
        print(msg, 'Capricórnio.')
elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        print(msg, 'Aquário.')
elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
        print(msg, 'Peixes.')
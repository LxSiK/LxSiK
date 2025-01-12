preco = 0
tamanho = input("Olá! Escolha o tamanho da pizza: [P, M, G ou GG] \n")
if tamanho == 'P':
   preco += 15
elif tamanho == 'M':
    preco += 20
elif tamanho == 'G':
    preco += 25
elif tamanho == 'GG':
    preco += 30

pepperoni = input("Gostaria de adicionar pepperoni? [S / N] \n")
if pepperoni == 'S' and tamanho == 'P':
    preco += 2
elif pepperoni == 'S' and tamanho == 'M':
    preco += 3
elif pepperoni == 'S' and tamanho == 'G':
    preco += 4
elif pepperoni == 'S' and tamanho == 'GG':
    preco += 5
    
queijo = input("Gostaria de adicionar queijo? [S / N] \n")
if queijo == 'S' and tamanho == 'P':
    preco += 2
elif queijo == 'S' and tamanho == 'M':
    preco += 3
elif queijo == 'S' and tamanho == 'G':
    preco += 4
elif queijo == 'S' and tamanho == 'GG':
    preco += 5

print(f'O preço final é ${preco}.')
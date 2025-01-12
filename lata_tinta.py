from math import ceil

def num_latas(altura, largura, cobertura):
    quantidade_latas = ceil((altura * largura)/cobertura)
    if quantidade_latas <= 1:
        quantia = 'lata'
    else:
        quantia = 'latas'
    print(f"Você precisará de {quantidade_latas} {quantia}.")

alt = int(input("Altura em m²: ")       )
lar = int(input("Largura em m²: "))
cob = 5
num_latas(altura = alt, largura = lar, cobertura=cob)
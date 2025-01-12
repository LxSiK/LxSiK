nomeum = input('Nome: ').lower()
nomedois = input('Nome: ').lower()

decimal = nomeum.count('a') + nomeum.count('m') + nomeum.count('o') + nomeum.count('r') + nomedois.count('a') + nomedois.count('m') + nomedois.count('o') + nomedois.count('r')  
numeral = nomeum.count('v') + nomeum.count('e') + nomeum.count('d') + nomeum.count('i') + nomedois.count('v') + nomedois.count('e') + nomedois.count('d') + nomedois.count('i')
resultado = (decimal * 10) + numeral

if resultado < 10 or resultado > 90:
    print(f'Sua compatibilidade é de {resultado}.\nVocês se dão tão bem quanto gato e rato.')
elif resultado >= 40 and resultado <= 50:
    print(f'Sua compatibilidade é de {resultado}%.\nVocês se dão bem juntos.')
else:
    print(f'Sua compatibilidade é de {resultado}%')

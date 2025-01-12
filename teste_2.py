alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']

def encode(code, key):
    n = 0
    letter = ''
    print("\nCodificando mensagem!\n")
    for x in code:
        if x not in alphabet:
            letter += x
        for y in alphabet:
            if y != x:
                n += 1
                if n + key >= len(alphabet):
                    n = - (len(alphabet)) - key
            else:
                n_final = n
                letter += (alphabet[n_final + key])
        print(n_final)
        new_code = [letter]
        n = 0
    print(f"A mensagem codificada é:" , ('').join(new_code))
    print(f"\nA chave é: {key}\n")

code = input("Mensagem: ").lower()
key = int(input("Chave: "))   

encode(code, key)
cont = 0
frase = input("Digite uma frase: ")

for i in frase:
    if i == 'a' or i == 'A':
        cont+=1

print(f"A frase possui {cont} letras A")
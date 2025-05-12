num = [""] *5
soma = 0

for i in range(5):
    num[i] = float(input(f"Digite o {i+1} número: "))
    soma += num[i]

media = soma / 5
print(f"A média é {media}")

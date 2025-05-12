num = [""] * 10
cont = 0

for i in range (len(num)):
    num = float(input(f"Digite o {i+1} número: "))
    if num > 50:
        cont += 1

print(f"Você digitou {cont} números maiores que 50")
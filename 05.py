num = [""] *5
soma = 0

for i in range(5):
    num[i] = float(input(f"Digite o {i+1} número: "))
    soma += num[i]

media = soma / 5

if media > 7:
    print(f"A média foi {media} e o aluno foi aprovado")
elif media < 4:
    print(f"A média foi {media} e o aluno foi reprovado")
elif media >= 4 < 7:
    print(f"A média foi {media}. Aluno em recuperação")
else:
    print("Número inválido")

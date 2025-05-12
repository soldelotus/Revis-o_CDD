import random

numSecreto = random.randint(1, 100)
num = None
cont = 0

while num!=numSecreto:

    num = int(input("Tente adivinhar o número secreto! Ele está entre 1 e 100. "
                    "\nDigite um número:"))
    cont+=1

    if num < numSecreto:
        print("O número secreto é maior...")

    if num > numSecreto:
        print("O número secreto é menor...")

    if num == numSecreto:
        print(f"Parabéns! Você acertou"
              f"\nFez {cont} tentativas")
senha = '1234'
digitada = None

while senha!=digitada:
    digitada = input("Digite a senha: ")

    if digitada == senha:
        print("Acesso liberado!")
    else:
        print("Acesso negado")
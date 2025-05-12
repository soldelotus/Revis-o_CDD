nomes = [""]*5

for i in range (len(nomes)):
    nomes[i] = input(f"Digite o {i+1} nome: ")

for j in nomes:
    if j[0] == 'a' or j[0] == 'A':
        print(j)





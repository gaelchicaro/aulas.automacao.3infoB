#Break: Interrompe o laço de repetição

nomes = ["aaa", "bbb","ccc","ddd"]

nomecomC = ""

for nome in nomes:
    if nome.startswith("c"):
        nomecomC = nome
        break
    print(nome)
    
print("O primeiro nome iniciado com C é ",nomecomC)

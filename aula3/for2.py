#estrutura for para percorrer listas
#listas são variáveis com mais de um valor

nomes = ["ivan", "Gael", "Mariana", "Isis"]

print(nomes,"\n")
print(nomes[2])
print("\n")

for i in range(4):
    print(nomes[i],end=" ")
print("\n")

for nome in nomes: #usando a lista como parametro de repetição
    print(nome)
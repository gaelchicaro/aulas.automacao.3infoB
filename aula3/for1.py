#estruturas de repetição

#for variavel in range(inicio, fim, tamanho do passo)
#for variavel in range(1, 10, 1) = 1,2,3,4,5,6,7,8,9
#for variavel in range(1, 10, 2) = 1,3,5,7,9

for i in range(1,10,1):
    print(i, end=" ")

print("\n")

for i in range(1,7,2):
    print(i,end=" ")
print("\n")
for i in range(0,-4,-1):
    print(i, end=" ")
print("\n")
#Se o inicio e o passo forem omitidos, o padrão é 0 de inicio e passo de 1
for i in range(10):
    print(i,end=" ")
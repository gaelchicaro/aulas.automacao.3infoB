#whille

continuar = True
contador = 0
alunos=['']

while continuar:
    
    print("Digte  o nome do aluno")
    aluno = input()
    alunos[contador] = aluno
    contador+=1

    resp = float(input("Deseja continuar: \n0 para NÃO \n1 para SIM"))
    if resp == 0:
        print("os alunos digitados são: ",alunos)
        break

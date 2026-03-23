#comando continue: Ignora  o restante dos comandos dentro do loop e continua do inicio na próxima interação
#dicionários são listas de listas

aluno1 = {"nome":"Gael","idade":18, "sexo":"M"}
aluno2 = {"nome":"Carlos","idade":18, "sexo":"M"}
aluno3 = {"nome":"Heitor","idade":17, "sexo":"M"}

#lista com dicionários
alunos= [aluno1, aluno2, aluno3]

for aluno in alunos:
    if aluno['idade'] >= 18:
        continue
    print("Olá", aluno['nome'], "qual é seu passatempo?")
    aluno['hobbie'] = input('')

print(alunos)
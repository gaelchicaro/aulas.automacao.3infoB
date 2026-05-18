import pandas as pd

#ler a  planilha do excel utilizando o Pandas
planilha = pd.read_excel('aula8/Alunos.xlsx')

#imprime a variavel planilha
print(planilha)

#Imprimir os dados do aluno Heitor
print(planilha.loc[2])


#imprimir só um dado
print(" ")
print(planilha.loc[3, "Alunos"])
print(" ")

#imprimir apenas dados selecionados
print(planilha.loc[0, ["Alunos", "Idade"]])

#Mudar os dados
planilha.loc[3, "Alunos"] = "locus"
print(planilha.loc[3,"Alunos"])

planilha.loc[3, ["Alunos", "Idade"]] = ["locus", 19]
print(planilha.loc[3])

#inserir dados (len(planilha coloca o tamanho da planilha para inserir na ultima linha))
planilha.loc[len(planilha), ["Alunos", "Idade", "gênero"]] = ["João", 32, "M"]
print(planilha)

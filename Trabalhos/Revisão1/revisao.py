#importar biblioteca
import pandas as pd

#carregar o exel
df = pd.read_excel("Trabalhos/Revisão1/planilha.xlsx")
print(df.head(3))#por padrão são 5
print(" ")

#LOCALIZAR DADOS    
#print(df.loc[0, "Nome"]) Seleciona linha , coluna
#print(df.loc[4 : 6, "Nome"]) Seleciona um intervalo de linhas e a coluna nome
#print(df.loc[4:6, ["Nome", "Idade"]]) Seleciona um intervalo de linhas e uma seleção de colunas
#rint(df.loc[ : , "Nome"]) Seleciona todas as linhas e uma coluna
#df2 = df.loc[3:6, ["Nome","Sexo"]] 
#print(df2.loc[[True,False,False,True]]) Seleciona por meio de valores bolean

#inserir novos dados na planilha
df.loc[len(df)] = ["Isis", "Feminino", 18, "Técnico em informática", "Automação", 10]
print(df.tail(2))#conta de baixo para cima

#Atualizar dados na planilha
df.loc[30, ["Curso", "Disciplina"]] = ["Artes", "Teatro"]
print(df.tail(2))

#Filtrar dados na planilha
condicao = df["Idade"] >= 20
condicao2 = df["Sexo"] == "Feminino"
print(df.loc[condicao & condicao2, "Nome"])

#Classificar dados 
tbl_ordenada=df.sort_values("Nome", ascending=True)#É necessário jogar para umavariável, mesmo que seja df=df.sort
print(tbl_ordenada)

#Contar dados
tbl_contagem = df.value_counts("Curso")
print(tbl_contagem)#vai dizer quantas pessoas estão em cada divisão

#Agrupar dados
tbl_agrupada = df.groupby("Disciplina")["Nota"].mean()#agrupa e o mean tira a média(pode ser outra coisa como o sum que soma)
print((tbl_agrupada))

#Exportar
df.to_excel("revisao\\nova_planilha.xls")
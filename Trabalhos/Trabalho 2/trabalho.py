import pandas as pd

lista = ("Trabalhos/Trabalho 2/notas_estudantes.xlsx")

df_notas = pd.read_excel (lista, sheet_name="Notas")
df_atividades = pd.read_excel (lista, sheet_name="Atividades")

df_notas.loc[df_notas.shape[0]] = {"Nome": 'Lucas Silva', "Atividade": 'Prova Final', "Nota": 8.5}

df_notas.loc[(df_notas["Nome"]=="Ana Souza") & (df_notas["Atividade"] == "Trabalho 1"),"Nota"] = 9.0

df_notas = df_notas.drop(df_notas[(df_notas["Nome"] == 'Pedro Santos') & (df_notas["Atividade"] == 'Prova 1')].index)

nta_7 = df_notas[df_notas["Nota"] > 7.0]

media = df_notas.groupby("Nome")["Nota"].mean()#o claude que passou esse código pq eu não tava conseguindo

nomenota = df_notas.loc[ :,["Nome", "Nota"]]

prvF = df_notas.loc[df_notas["Atividade"] == 'Prova Final']

nome7 = nta_7.loc[:,["Nome","Atividade"]]

df_notas = df_notas.sort_values(by="Nome", ascending=True)

combinacao = pd.merge(df_notas , df_atividades, on="Atividade")

df_notas.to_excel("aulas.automacao.3infoB/Trabalhos/Trabalho 2/notas_estudantes_ordenado.xlsx", index=False)

print(df_atividades)
print(df_notas)
print(nta_7)
print(media)
print(nomenota)
print(prvF)
print(nome7)
print(combinacao)
print(df_notas)
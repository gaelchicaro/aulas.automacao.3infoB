import pandas as pd

lista = ("Trabalhos/Trabalho 2/notas_estudantes.xlsx")

df_notas = pd.read_excel (lista, sheet_name="Notas")
df_atividades = pd.read_excel (lista, sheet_name="Atividades")
print(df_atividades)
print(" ")
print(df_notas)
print(" ")

#funciona o loc[len(df_notas)]
df_notas.loc[df_notas.shape[0]] = {"Nome": 'Lucas Silva', "Atividade": 'Prova Final', "Nota": 8.5}


df_notas.loc[(df_notas["Nome"]=="Ana Souza") & (df_notas["Atividade"] == "Trabalho 1"),"Nota"] = 9.0


df_notas.drop(df_notas[(df_notas["Nome"] == 'Pedro Santos') & (df_notas["Atividade"] == 'Prova 1')].index, inplace=True)


nta_7 = df_notas.loc[df_notas["Nota"]> 7.0 ]


media = df_notas.groupby("Nome")["Nota"].mean()#o claude que passou esse código pq eu não tava conseguindo


nomenota = df_notas.loc[ :,["Nome", "Nota"]]


prvF = df_notas.loc[df_notas["Atividade"] == 'Prova Final']


nome7 = nta_7.loc[:,["Nome","Atividade"]]


df_notas = df_notas.sort_values(by="Nome", ascending=True)


combinacao = pd.merge(df_notas , df_atividades, on="Atividade")


df_notas.to_excel("Trabalhos/Trabalho 2/notas_estudantes_ordenado.xlsx", index=False)


print(nta_7)
print(" ")
print(media)
print(" ")
print(nomenota)
print(" ")
print(prvF)
print(" ")
print(nome7)
print(" ")
print(combinacao)
print(" ")
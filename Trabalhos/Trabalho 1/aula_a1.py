import pandas as pd

tabela = pd.read_excel("estudantes.xlsx")

tabela.iloc[:5, :4]

tabela.loc[3] = {'RA': '5','Nome': 'Enzo Moreira', 'Curso': 'Técnico em Jogos', 'Turma': '1GMA'}

tabela.at[3, 'Curso'] = 'Técnico em Informática'
tabela.at[3, 'Turma'] = '3TE'

tabela = tabela.drop([1])

tabela.to_excel("estudantes_atualizado.xlsx", index=False)


print(tabela)

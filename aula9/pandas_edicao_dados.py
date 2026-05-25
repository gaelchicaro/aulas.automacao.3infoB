#Pandas: Biblioteca em Python que permite a manipulação de arquivos em formato tabular, ex: planilhas e tabelas.

#Edição de dados (inserir, atualizar e excluir)

#importar biblioteca (as renomeia o pacote abreviação)

import pandas as pd

#ler uma planilha do exel
#Cria a variavel planilha que vai guardar a planilha do exel 
#Em pandas chamamos a planilha dde DataFrame
planilha = pd.read_excel("aula9/Dados 3INFOB.xlsx")

#mostra todos os dados da planilha
#print(planilha)

#imprime a cabeça da planilha: Quantas linhas da parte de cima eu quero
#print(planilha.head(3))

#imprimir as ultimas 5 linhas
#print(planilha.tail(5))

#plla = planilha.head(4)
#print(plla.tail(2))

#inserir um novo registro na planilha
#planilha.loc[len(planilha)] = ['Pablo', 52, 1.80, 'M']
#print(planilha)

#Atualizar registro
planilha.loc[16] = ['Pablo', 53, 1.80, 'Masculino']
print(planilha)

#Atualizar registro, apenas uma coluna
planilha.loc[16, 'Nome'] = 'Pablo Sandi'
print(planilha)

#Atualizar registro, de duas ou mais colunas
planilha.loc[16, ['Peso', 'Altura']] =[54, 1.81]
print(planilha)

#Remover o registro
#planilha = planilha.drop(13)
#ou 
planilha.drop(13, inplace=True)
print(planilha)
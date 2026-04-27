from aula4.funcao import imprimir
from aula4.funcao import ler, PulaLinha,somar


#usando as funções
imprimir("digite o número 1")
n1= ler()

PulaLinha()
PulaLinha()

imprimir('digite o número 2')
n2 = ler()

resposta = somar(n1,n2)
imprimir(f"O resultado é: {resposta}")
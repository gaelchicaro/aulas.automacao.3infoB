import aula4.funcao as litos #pode ser o nome que quiser, o normal é vir como o nome do arquivo. Nesse o nome base era funcao


#usando as fuções
litos.imprimir("digite o número 1")
n1= litos.ler()

litos.PulaLinha()
litos.PulaLinha()

litos.imprimir('digite o número 2')
n2 = litos.ler()

resposta = litos.somar(n1,n2)
litos.imprimir(f"O resultado é: {resposta}")
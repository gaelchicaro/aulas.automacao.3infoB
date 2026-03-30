

#duas entradas uma saída(return)
def somar( n1, n2):
    return n1+n2

#uma entrada, sem saída
def imprimir(texto):
    print(texto)

#sem entrada sem saída
def PulaLinha():
    print('\n')

def ler():
    return int(input())

imprimir("digite o número 1")
n1= ler()

imprimir('digite o número 2')
n2 = ler()

resposta = somar(n1,n2)
imprimir(f"O resultado é: {resposta}")
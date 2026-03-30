SalarioB=float(input('Digite seu salário bruto '))

PrctgmINSS=(11/100)*SalarioB
PrctgmFGTS=(7.5/100)*SalarioB
SalarioL=SalarioB-PrctgmINSS-PrctgmFGTS
Descontos=PrctgmINSS+PrctgmFGTS

print('O salário líquido é: ',SalarioL,'R$')
print('O desconto do INSS é: ',PrctgmINSS)
print('O desconto do FGTs é: ',PrctgmFGTS)
print('O desconto total é: ',Descontos)
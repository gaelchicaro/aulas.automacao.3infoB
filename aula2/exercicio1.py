
#entrada
nota1 = float(input("Digite sua primeira nota"))
nota2 = float(input("Digite sua segunda nota"))

#processamento
media = (nota1+nota2)/2

if media >= 6:
    print("Aprovado")
else:
    nota3 = float(input('Digite a nota do exame final'))
    media = (media + nota3)/2
    if media >= 6:
        print('Aprovado')
    else:
        print('Reprovado')
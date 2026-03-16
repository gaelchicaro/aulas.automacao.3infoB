
#entrada
nota1 = float(input("Digite sua primeira nota"))
nota2 = float(input("Digite sua segunda nota"))

#processamento
media1 = (nota1+nota2)/2

if media1 >= 6:
    print("Aprovado")
else:
    nota3 = float(input('Digite a nota do exame final'))
    mediaf = (media1 + nota3)/2
    if mediaf >= 6:
        print('Aprovado')
    else:
        print('Reprovado')
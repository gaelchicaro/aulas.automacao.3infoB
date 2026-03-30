
while True:
    try:
        a=int(input("digite um numero"))
        b=int(input("digite outro número"))
        print("resultado: ",a/b)
        break
    except ValueError:
        print("O valor digitado é inválido")
    except ZeroDivisionError:
        print("Não é possível dividir por zero")
    except Exception as e:
        print("Ocorreu um erro\n",e)
        
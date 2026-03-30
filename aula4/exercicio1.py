continuar = True

while continuar:
    usuario = input(" Digite seu nome de usuário: ")
    senha = input("Digte sua senha: ")

    if (usuario == "admin" and senha == "admin123"):
        print("Bem vindo")
        break
    else:
        print("Digite a senha e o usuario corretos")


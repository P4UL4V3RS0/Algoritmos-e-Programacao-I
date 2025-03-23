print("Opções")
print("0 - Sair")
print("1 - Cadastrar")
print("2 - Consultar")

Opcao=int(input("Escolha uma das opções: "))
while Opcao!=0:
    if Opcao==1:
        Nome=str(input("Digite o seu nome: "))
        Idade=int(input("Digite a sua idade: "))
        Telefone=int(input("Digite o seu telefone: "))
    elif Opcao==2:
        print("O nome cadastrado é: ",Nome)
        print("A idade cadastrada é: ",Idade)
        print("O telefone cadastrado é",Telefone)
    else:
        break
    Opcao=int(input("Escolha uma das opções: "))
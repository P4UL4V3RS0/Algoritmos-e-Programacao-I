tentativas=3
usu="paula"
sen=123
usuario_cliente=str(input("Digite seu nome de usuário: "))
senha=int(input("Digite sua senha: "))
saldo=0


menu=f"""
----------Principal-----------
Olá, {usuario_cliente}
Seja bem vindo ao nosso sistema bancário.
O que deseja fazer?

0 - SAIR
1 - CONTA POUPANÇA
2 - CONTA CORRENTE

"""

menu_funcoes=f"""
----------Principal-----------
Olá, {usuario_cliente}

O que deseja fazer?

0 - SAIR
1 - DEPÓSITO 
2 - SAQUE
3 - EXTRATO

"""

while tentativas<=3:
    if usuario_cliente==usu and senha==sen:
        print(menu)
        opcao=int(input("Escolha uma opção: "))
        while True:
            if opcao==0:
                exit()
            elif opcao==1:
                print(menu_funcoes)
                opcao_funcoes=int(input("Escolha uma opção: "))
                while True:
                    if opcao_funcoes==0:
                        exit()
                    elif opcao_funcoes==1:
                            deposito=int(input(f"Digite o valor do depósito: "))
                            saldo += deposito
                            print(f'o valor do depósito é R$ {deposito}')
                            break
                    elif opcao_funcoes==2:
                        saque=int(input(f'Digite o valor do saque: '))
                        if saldo>=saque:
                        
                            saldo -= saque
                            print(f"o valor sacado é R$ {saque}")
                            break
                        else:
                            print("Saque não autorizado, valor de saque maior que o valor de saldo.")
                            print("Por favor faça um depósito!")
                            break
                    elif opcao_funcoes==3:
                        print(f"Seu saldo atual é igual a: R$ {saldo}")
                        break
                    else:
                        opcao_funcoes=int(input("Escolha uma opção: "))
            elif opcao==2:
                print(menu_funcoes)
                opcao_funcoes=int(input("Escolha uma opção: "))
                while True:
                    if opcao_funcoes==0:
                        exit()
                    elif opcao_funcoes==1:
                            deposito=int(input(f"Digite o valor do depósito: "))
                            saldo += deposito
                            print(f'o valor do depósito é R$ {deposito}')
                            break
                    elif opcao_funcoes==2:
                        saque=int(input(f'Digite o valor do saque: '))
                        if saldo>=saque:
                        
                            saldo -= saque
                            print(f"o valor sacado é R$ {saque}")
                            break
                        else:
                            print("Saque não autorizado, valor de saque maior que o valor de saldo.")
                            print("Por favor faça um depósito!")
                            break
                    elif opcao_funcoes==3:
                        print(f"Seu saldo atual é igual a: R$ {saldo}")
                        break
                    else:
                        opcao_funcoes=int(input("Escolha uma opção: "))
            else:
                print("aqui ficará as outras opções")
    elif tentativas==1:
        print("usuário bloqueado")
        break
    elif tentativas>1:
        tentativas-=1
        print(f"Você tem mais {tentativas} tentativas")
        usuario=str(input("Digite seu nome de usuário: "))
        senha=int(input("Digite sua senha: "))
    else:
        break


tentativas=3
usu="paula"
sen=123
usuario_cliente=str(input("Digite seu nome de usuário: "))
senha_cliente=int(input("Digite sua senha: "))
clientes=[]
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
Seja bem vindo ao nosso sistema bancário.
O que deseja fazer?

0 - SAIR
1 - DEPÓSITO 
2 - SAQUE
3 - EXTRATO

"""

while tentativas<=3:
    if usuario_cliente==usu and senha_cliente==sen:
        print(menu)
        opcao=int(input("Escolha uma opção: "))
        while True:
            if opcao==0:
                exit()
            elif opcao==1:
                print(menu_funcoes)
                while True:
                    opcao_funcoes=int(input("Escolha uma opção: "))
                    
                    if opcao_funcoes==0:
                        exit()
                    elif opcao_funcoes==1:
                        deposito=int(input(f"Digite o valor do depósito: "))
                        print(f'o valor do depósito é R${deposito}')
                        print(menu_funcoes)
                        saldo += deposito
                    elif opcao_funcoes==2:
                        if saldo>0:
                            
                            saque=int(input(f'Digite o valor do saque: '))
                            if saque>saldo:
                                print("Valor não autorizado")
                

                            print(f'o valor do saque é R${saque}')
                            
                            saldo -= saque
                            print(menu_funcoes)
                        else:
                            print("Deposite um valor")
                            print(menu_funcoes)
                    elif opcao_funcoes==3:
                        print(saldo)
                        print(menu_funcoes)
                    else:
                        print(menu_funcoes)

            elif opcao==2:
                print(menu_funcoes)
                exit()
            else:
                clientes.append(cliente)
                opcao=int(input("Escolha uma opção: "))
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
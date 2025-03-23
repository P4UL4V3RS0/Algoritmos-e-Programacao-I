tentativas=3
usu="paula"
sen=123
usuario_cliente=str(input("Digite seu nome de usuário: "))
senha=int(input("Digite sua senha: "))
saldo=0
def deposito(saldo):
    valor_deposito=int(input("Digite o valor de depósito: "))
    valor_deposito+=0
    return valor_deposito
def saque(saldo):
    valor_saque=int(input("Digite o valor de depósito: "))
    valor_saque-=0
    return valor_saque


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
                        def deposito():
                            return deposito
                            print("o valor depositado é R$ {valor_depositado}")
                    elif opcao_funcoes==2:
                        if saldo>=saque:
                            def saque():
                                print("o valor sacado é R$ {valor_depositado}")
                        else:
                            print("Saque não autorizado, valor de saque maior que o valor de saldo.")
                    elif opcao_funcoes==3:
                        print(saldo)
                    else:opcao_funcoes=int(input("Escolha uma opção: "))

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


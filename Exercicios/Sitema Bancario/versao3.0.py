tentativas=3
usu="paula"
sen=12345
usuario=str(input("Digite seu nome de usuário: "))
senha=int(input("Digite sua senha: "))

menu=f"""
----------Principal-----------
Olá, {usuario}
Seja bem vindo ao nosso sistema bancário.
O que deseja fazer?

0 - SAIR
1 - CADASTRAR CLIENTE
2 - CRIAR CONTA

"""

while True:
    if usuario==usu and senha==sen:
        print(menu)
        break
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


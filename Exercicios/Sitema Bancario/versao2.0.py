usu="paula"
sen=12345

usuario=str(input("Digite seu nome de usuário: "))
senha=int(input("Digite sua senha: "))

menu=f"""
----------Principal-----------
Olá, {usuario}
Seja bem vindo ao nosso sistema bancário.
O que deseja fazer?

1 - CADASTRAR CLIENTE
2 - CRIAR CONTA

"""

if usuario==usu and senha==sen:
    print(menu)
else:
    print("Usuário ou senha INCORRETO")
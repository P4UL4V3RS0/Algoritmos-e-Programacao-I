tentativas=3
usu=["paula","paulo","lucas"]
sen=[1234,2424,1313]
usuario=str(input("Digite seu nome de usuário: "))
senha=int(input("Digite sua senha: "))
clientes=[]

menu=f"""
----------Principal-----------
Olá, {usuario}
Seja bem vindo ao nosso sistema bancário.
O que deseja fazer?

0 - SAIR
1 - CADASTRAR CLIENTE
2 - CRIAR CONTA
3 - TROCAR DE USUÁRIO
"""

# while tentativas<=3:
for i, item in enumerate(usu):
    if item == usuario:
        if sen[i] == usuario:
            print(menu)
            opcao=int(input("Escolha uma opção: "))
            while True:
                if opcao==1:
                    nome=str(input("Digite o nome do cliente que se quer cadastrar: "))
                    idade=int(input("Digite a idade do cliente que se quer cadastrar: "))
                    tel_fixo=int(input("Digite o telefone fixo do cliente que se quer cadastrar: "))
                    tel_cel=int(input("Digite o telefone celular que se quer cadastrar: "))
                    tel_recado=int(input("Digite o telefone para recado que se quer cadastrar: "))
                    cliente=[nome,idade,[tel_fixo,tel_cel,tel_recado]]
                        
                    print(f"os dados do cliente cadastrado são {cliente}")
                    opcao=int(input("Escolha uma opção: "))
                elif opcao==2:
                    novousu=str(input("Digite o nome do novo usuário: "))
                    novasen=int(input("Digite a nova senha: "))
                elif opcao==3:
                    usuario=str(input("Digite seu nome de usuário: "))
                elif opcao==0:
                    exit()
                else:
                    clientes.append(cliente)
                    opcao=int(input("Escolha uma opção: "))
        if tentativas==1:
            print("usuário bloqueado")
            break
        elif tentativas>1:
            tentativas-=1
            print(f"Você tem mais {tentativas} tentativas")
            usuario=str(input("Digite seu nome de usuário: "))
            senha=int(input("Digite sua senha: "))
        else:
            break


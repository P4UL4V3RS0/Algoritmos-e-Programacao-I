class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha
        self.tentativas = 0
        self.bloqueado = False

    def autenticar(self, senha_digitada):
        if self.bloqueado:
            return "Usuário Bloqueado"

        if senha_digitada == self.senha:
            self.tentativas = 0
            return "Acesso permitido"
        else:
            self.tentativas += 1

            if self.tentativas >= 3:
                self.bloqueado = True
                return "Usuário Bloqueado"
            else:
                return f"Senha incorreta. Tentativas restantes: {3 - self.tentativas}"

def main():
    usuarios = {
        "joao": Usuario("João", "1234"),
        "maria": Usuario("Maria", "abcd")
    }

    while True:
        nome = input("Digite seu nome de usuário: ")
        usuario = usuarios.get(nome)

        if usuario is None:
            print("Usuário não encontrado.")
            continue

        senha_digitada = input("Digite sua senha: ")
        resposta = usuario.autenticar(senha_digitada)
        print(resposta)

        if resposta == "Acesso permitido" or resposta == "Usuário Bloqueado":
            break

if __name__ == "__main__":
    main()


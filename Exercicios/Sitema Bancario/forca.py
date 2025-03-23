
import random

palavras = ["maçã", "banana", "laranja", "uva", "abacate"]

palavra_secreta = random.choice(palavras)
letras_acertadas = ["_"] * len(palavra_secreta)
tentativas = 6

while tentativas > 0:
    print(" ".join(letras_acertadas))
    chute = input("Chute uma letra: ").lower()

    if chute in palavra_secreta:
        for i, letra in enumerate(palavra_secreta):
            if letra == chute:
                letras_acertadas[i] = chute
    else:
        tentativas -= 1
        print(f"Errou! Restam {tentativas} tentativas.")

    if "_" not in letras_acertadas:
        print(" ".join(letras_acertadas))
        print("Você ganhou!")
        break
else:
    print(f"Você perdeu! A palavra era {palavra_secreta}.")


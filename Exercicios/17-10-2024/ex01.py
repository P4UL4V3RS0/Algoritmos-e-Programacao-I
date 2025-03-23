soma=0
palavra=str(input("Digite uma palavra: "))

for cont in palavra:
    if cont in "aeiou":
        soma+=1
print(f"A quantidade de vogais é {soma}")
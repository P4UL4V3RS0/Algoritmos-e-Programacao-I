nota1=int(input("Digite a nota 1: "))
nota2=int(input("Digite a nota2: "))

media=nota1+nota2/2

if media>0 or media<10:
    if media>=7:
        print("Aprovado")
    elif media==10:
        print("Aprovado com distinção")
    else:
        print("Reprovado")
    nota1=int(input("Digite a nota 1: "))
    nota2=int(input("Digite a nota2: "))
else:
    print("Digite uma nota entre 0 e 10")
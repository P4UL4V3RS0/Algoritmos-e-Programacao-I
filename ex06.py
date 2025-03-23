numero1=int(input("escreva o número 1: "))
numero2=int(input("escreva o número 2: "))
numero3=int(input("escreva o número 3: "))

while numero1 != numero2 and numero2 != numero3 and numero3 != numero1:

    if numero1 > numero2 and numero1 > numero2:
        print(numero1)
    elif numero2 > numero1 and numero2 > numero3:
        print(numero2)
    elif numero3 > numero1 and numero3 > numero2:
        print(numero3)
    else:
        print("")
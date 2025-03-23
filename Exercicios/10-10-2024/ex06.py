cont=1
maior=0

while cont<=5:
    num=int(input("Digite o número: "))

    if num>maior:
        maior=num
    cont+=1
print(maior)
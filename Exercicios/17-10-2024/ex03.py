par=0
imp=1

for cont in range(10):
    num=int(input(f"Digite o nº {cont+1}: "))

    if num%2==0:
        par+=1
    else:
        imp+=1
print(f"A quantidade de nº pares é {par} e de impares é {imp}")
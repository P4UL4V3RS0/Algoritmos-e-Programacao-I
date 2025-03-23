num1=int(input("Digite um número: "))
num2=int(input("Digite outro número: "))

if num1<=num2:
    while num1<=num2:
        print(num1)
        num1+=1
else:
    while num2<=num1:
        print(num2)
        num2+=1
        
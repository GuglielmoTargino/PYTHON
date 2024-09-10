

print('Calculadora popular em python')
print('escolha uma operação para calcular ')
print('1-adição, 2-subtração, 3-multiplicação, 4-divisão')

oper=int(input('digite a operação escolhida'))
num1=int(input('digite o primeiro nu mero'))
num2=int(input('digite o segundo numero'))

if(not(num2==0)):

    if(oper==1):
        print(num1+num2)
    elif(oper==2):
        print(num1-num2)
    elif(oper==3):
        print(num1*num2)
    else:
        print(num1/num2)
    
else:
    print('divisor não pode ser 0')


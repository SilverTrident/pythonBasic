"""
isnumeric9() isdecimal() isdigit() verificam se são numeros e retornam true or false
so verificao numeros interios positivos
"""
num1 = input('Digite um numero ')
num2 = input('Digite outro numero ')

if num1.isnumeric() and num2.isnumeric():
    print('São numeros')
else:
    print('não são numeros')

## maneira de fazer cast correta

try:
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
except:
    print('err')
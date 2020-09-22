#Digitar numero inteiro informar se é par ou impar e se é inteiro

numero = input('digite um numero inteiro ')

if numero.isnumeric():
    numero = int(numero)

    if numero % 2 == 0 :
        print('Seu numero é par')
    else:
        print('seu numero é impar')
else:
    print('não é um numero')

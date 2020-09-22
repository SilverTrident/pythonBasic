#digitar se o tamanho do nome da pessoa  é grande 7 ou mais pequeno 4 letras ou menos ou normal 5-6
nome = input('Digite seu nome ')

number_letters = len(nome)

if number_letters <= 4 and number_letters > 0:
    print("Nome é curto")
elif number_letters == 5 or number_letters == 6:
    print('Nome normal')
elif number_letters > 6:
    print('Nome é grande')
else:
    print('erro')
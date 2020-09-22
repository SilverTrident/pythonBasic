
frase = 'meu nome e Filipe'

cont = 0
nova_strin = ''

while cont < 17:

    if frase[cont] == 'F':
        nova_strin += 'f'
    else:
        nova_strin += frase[cont]

    cont += 1

print(nova_strin)
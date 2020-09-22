#programa pergunte a hora e inoforme se é manhã 0-11 tarde 12-17 noite 18-23

hora = input('Digite a Hora atual: ')

if hora.isnumeric() :
    hora = int(hora)
    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Bom tarde')
    elif hora >= 18 and hora <= 23:
        print('Bom Noite')
    else:
        print('err')
else:
    print('CARACTERE digitado invalido')

  # if respone a uma ierarquia como visto a abixo tudo que esta identado internamente pertence ao bloco superior
"""
f True:
    print('Execulta o primeiro bloco')
elif False:
    print('execulta')
    print('execulta tudo na ierarquia')
else:
    print('tudo falso')

if False:
    print('não execulta pois esta identado')
print('execulta pois nao esta no if')
"""

idade = int(input('Digite sua idade '))


if idade >= 18:
    print('Você é maior de idade')
elif idade < 18:
    print('Você e menor de idade')
else:
    print('err')
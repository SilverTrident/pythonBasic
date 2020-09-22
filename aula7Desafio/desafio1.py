
nome = 'Filipe'
idade = 23
ano_atual = 2020

altura = 1.83
peso = 74

ano_nasc = ano_atual - idade
imc = peso/altura**2

print(f'{nome} tem {idade} de idade e naasceu em {ano_nasc}'
      f'\n tem peso de {peso} e altura de {altura} com imc: {imc:.2f}')
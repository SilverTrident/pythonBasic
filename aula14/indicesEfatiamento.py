texto  = 'python'

  # incie são os valores dos arrys das strings inidces positivos
print(texto[0],texto[1],texto[2],texto[3],texto[4],texto[5],sep='')

  # indice neegativo
print(texto[-1],texto[-2],texto[-3],texto[-4],texto[-5],texto[0],sep='')

  # intervalo de indice
intervalo = texto[1:5]
print(intervalo)

# pular(step) incides de indices

pular = texto[1::2]  # pula de 2 em dois
print(pular)
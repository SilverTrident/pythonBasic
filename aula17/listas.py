"""
.startswith('F') - começa com
for/else 
l1.extend(l2) entede outra lista
l1.apend('adiona novo valor')
l1.insert(0, 'valor) inseri na posição do arry o valor
l1.pop() remove o ultimo elmento
del(l1[valor])
print(max(l4)) retorna maior valor de uma lista de numericos
print(min(l4)) retorna menor valor de uma lista de numericos
l5 = list(range(1,50)) - cria uma lista de 1  ate 50
"""
lista = ['a', 'b','c','d','e']
junta_array = ''


for n in lista:
    junta_array += n

print(junta_array)
print('\n\n')

li1 = [1,2,3]
li2 = [4,5,6]
l3 = li1+li2
print(l3)

l1 = ['a','bacate',25]
l1.extend(l3)
print(l1)
l1.append('mais um valor adicionado')
print(l1)
l1.insert(4, 'inserido na posição 4')
print(l1)
l1.pop()
print(l1)
  # del(l1[5:8])
print(l1)
l4 = [99,25,3,4,5,18,7,8,9]
print(max(l4))
print(min(l4))

l5 = list(range(1,50))
print(l5)

lista1 = ['ilipe Souza', 'Ismael Souza', "nome qualquer"]

for response in lista1:
    if response.startswith('F'):
        print(response)
        break
else:
    print('nada foi achado')

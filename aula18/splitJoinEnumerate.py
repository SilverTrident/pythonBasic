"""
    .split(' ') - divide uma str pode se coocar um rejex
    .captalize() - deiza a primera letra em maisculo
    .count(n) - conta aquantidade de vezes que a palavra se repete
    ' '.join(lista) junta em uma string separando os valores por espaço
    enumerate(lista) - enumera um valor da lista
"""

string =  'passar os valores para array passar mais de um valor passar'
lista = string.split(' ')
print(lista)

for n in lista:
    print(f'a palavra {n} apareceu {lista.count(n)}x na frase')

lista = ' '.join(lista)
print(lista)

for index, valor in enumerate(lista):
    print(index, valor)

listas = [
    [0, "Primerio"],
    [1, "segundo"],
    [3, "Terceiro"],
]
print(listas)
for lis,tring in listas:
    print(lis, tring)
n1, n2, n3 = listas
print(n1, n2, n3)

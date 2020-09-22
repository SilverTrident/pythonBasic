"""
F string colocar variaveis por cochetes - coloque f antes de iniciar ''

"""

nome = "Filipe"
idade = 23
pi = 3.14159265359

# passsar pelo f
print(f'{nome} tem uma idae de {idade} o numeor de pi é {pi:.2f}')

# .format
print('{} tem uma idae de {} o numeor de pi é {:.2f}'.format(nome, idade, pi))

#.format posição
print('{2} tem uma idae de {2} o numeor de pi é {2:.2f}'.format(nome, idade, pi))

# .format atribuição
print('{n} tem uma idae de {i} o numeor de pi é {p:.2f}'.format(n=nome, i=idade, p=pi))

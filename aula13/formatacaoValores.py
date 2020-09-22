"""
Firmatando valores com modificadores

:s - texto (String)
:d - Inteiros
:f - float
:.(numero)f - quantidade de casas
:(CARACTERE(> ou < ou )^(qauntidade de casas)(Tipo - s,d ou f))

> - Esquerda
< - direita
^ - Centro

"""
nome ="Filipe souza"

print(nome.lower())
print(nome.upper())
print(nome.title()) # primeiras letras maiusculas

num = 1996
print(f'{num:|<10}')
print(f'{num:|>10}')
print(f'{num:|^10}')
print(f'{num:.2f}')
print(f'{num:|^10.2f}')
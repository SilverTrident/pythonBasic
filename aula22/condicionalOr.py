name = input('Digite seu nome')
if name:
    print(name)
else:
    print("nao digitou nada")

print(name or 'nada digitado utilizando or')
a = 0
b = None
c = False
d = []
e = {}
f = ""
g = 'Filipe'
variavel = a or b or c or d or f or e or f or g
print(variavel)
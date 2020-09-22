listas = [
    [0, "Primerio"],
    [1, "segundo"],
    [4, "Terceiro"],
    [5, "quarto"],
    [6, "quinto"],
    [7, "sexto"],
]
print(listas)


n1,*outra_lista, ultimo = listas
print(n1, 'variaveis diferente ',outra_lista, 'ultimo item',ultimo)
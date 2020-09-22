texto = 'pyton'

for i in texto:  # varre array texto e retorna em in o numero de vezes
    print(i)

for n, i in enumerate(texto):  #unumera cada repetição
    print(n, i)

  # função range(start, stop, step) step (pular)
for n in range(1, 10):
    print(n)
for n in range(20, -1, -1):
    print(n)

nova_strin = ''
for n in texto:
    if n == 't':
        # continue # remove a letra t
        nova_strin += n.upper()
    else:
        nova_strin += n
print(nova_strin)
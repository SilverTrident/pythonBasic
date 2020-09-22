"""
Operadores logicos and or not

opradores in - not in (in - se contem retorna verdadeiro, not in - se nao contem retona verdadeiro)
"""
verdade = True
falso = False
nome = 'filipe'


if verdade and falso:
    print('Verdade e falso nao execultam')
elif verdade and verdade:
    print('execulta verdadeiro')
if falso or verdade:
    print('execulta pois um é verdadeiro')
if falso or falso:
    print('nao execulta pois os dois são falsos')
if not falso and falso:
    print('naõ execulta pois um é falso')
if not falso and not  falso:
    print('execulta pois os dois são verdadeiros')
if 'f' in nome:
    print(f'existe a letra f no nome {nome}' )
if 'u' not in nome:
    print(f'não contem a letra u no nome {nome}')
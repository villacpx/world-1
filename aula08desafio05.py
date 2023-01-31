import random
n1 = str(input('Primeiro aluno '))
n2 = str(input('Segundo aluno '))
n3 = str(input('Terceiro aluno '))
lista = [n1, n2, n3]
random.shuffle(lista)
print(f'A ordem de apresentação será {lista}.')
n4 = str('Gabriel')
n5 = str('Tam')
n6 = str('Gabi')
lista2 = [n4, n5, n6]
random.shuffle(lista2)
print(f'A segunda ordem de apresentação será {lista2}')

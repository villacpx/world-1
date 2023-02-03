import random
a = random.randint(0, 10)
b = random.randint(0, 10)
c = random.randint(0, 10)
print(a, b, c)
if a <= b and a <= c:
    menor = a
if b <= a and b <= c:
    menor = b
if c <= a and c <= b:
    menor = c
print(f'O menor número é {menor}')
if a >= b and a >= c:
    maior = a
if b >= a and b >= c:
    maior = b
if c >= a and c >= b:
    maior = c
print(f'e o maior número é {maior} ')
if a == b and a == c:
    igual = a
if b == a and b == c:
    igual = b
if c == a and c == b:
    igual = c
    print('e todos os números são iguais')
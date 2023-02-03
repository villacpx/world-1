import random
print('veja se seus números formam um triângulo')
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro numero: '))
n3 = float(input('Agora o último número: '))
#erro1 if n1 < n2+ n3 and n2 < n1 + n3 OR n3 < n2 + n1:
if n1 < n2+ n3 and n2 < n1 + n3 and n3 < n2 + n1:
    print('essas medidas conseguem formar um triângulo!')
else:
    print('Essas medidas não formam um triângulo!')

a = random.randint(1, 10)
b = random.randint(1, 10)
c = random.randint(1, 10)
#erro1 if n1 < n2+ n3 and n2 < n1 + n3 OR n3 < n2 + n1:
print(a, b, c)
if a < b + c and b < a + c and c < a + b:
    print('essas medidas conseguem formar um triângulo!')
else:
    print('Essas medidas não formam um triângulo!')

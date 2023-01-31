import math
print('Mostrar o cosseno, tangente e seno')
n = float(input('Digite o ângulo '))
print(f'O cosseno é {math.cos(n)}, seu tangente é {math.tan(n)} e seno é {math.sin(n)}')
print('Primeira tentativa = erro')
n1 = float(input('Digite um ÂNGULO: '))
print(f'Seu Seno é {math.sin(math.radians(n1)):.2f}, Cosseno é {math.cos(math.radians(n1)):.2f} \n seu tangente é {math.tan(math.radians(n1)):.2f}')

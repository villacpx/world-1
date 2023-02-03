import random
n1 = random.randint(0, 5)
r = (int(input('Tente adivinhar o número de 0 a 5 em que o computador está pensando. ')))
if n1 == r:
    print('Parabéns, você acertou!')
else:
    print('Errou feio, tente novamente!')
print(f'Aqui está o número em que o computador pensou: {n1}')

import random
km = random.randint(65, 100)
if km >80:
    print(f'Você passou acima do limite! Recebeu R${(km-80)*7}')
else:
    print('Você não passou do limite, parabéns!')
print(f'Sua velocidade: {km}')
print(f'O quanto você recebeu de multa: R${(km-80)*7}')

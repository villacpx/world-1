km = int(input('Quantos quilômetros tem sua viagem? '))
if km <= 200:
    print(f'Sua viagem sairá {km*0.5:.2f}')
else:
    print(f'Sua viagem sairá {km*0.45:.2f}')

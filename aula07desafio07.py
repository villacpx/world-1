print('O QUANTO DE TINTA É NECESSÁRIO PARA PINTAR SUA PAREDE?')
altura = float(input('Digite a altura da sua parede '))
largura = float(input('Agora, digite a largura da sua parede '))
quantidade = ((altura*largura)/2)
print(f'A área da sua parede é {altura*largura:.2f}m²')
print('Cada lata de tinta da nossa empresa cobre 2m²')
print(f'A quantidade de latas exata será de {quantidade:.1f}')

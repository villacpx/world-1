cidade = str(input('Digite o nome de sua cidade: '))
cidade = cidade.title().split()
print(cidade)
santo = ('Santo' in cidade[0])
print(f'Sua cidade possuí a primeira palavra "santo"? r: {santo}')

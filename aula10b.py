nome = str(input('Qual é o seu nome? '))
nome2 = nome.title()
if nome2.find('nathan'):
    print('Que nome estranho')
else:
    print('Que nome normal')
print(f'bom dia, {nome2}')

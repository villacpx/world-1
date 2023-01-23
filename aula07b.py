print('ORDEM DOS OPERADORES, DENTRO DO PARENTESES EXECUTA PRIMEIRO.')
print('SEGUNDO POTÊNCIA, TERCEIRO É MULTIPLICAÇÃO, DIVISÃO, DIVISÃO INTEIRA E RESTO DE DIVISÃO')
print('ÚLTIMO É ADIÇÃO E SUBTRAÇÃO.')

print(5+3*2)
print(3*5+4**2)
print(3*(5+4)**2)

nome = input('Qual é o seu nome?  ')
print(f'Prazer em te conhecer {nome:<20}!')
print(f'Prazer em te conhecer {nome:>20}!')
print(f'Prazer em te conhecer {nome:^20}!')

numero_grande = float(input('número '))
multi = (numero_grande*13567)
print(f'o número grande resumido é {multi:.3f}')

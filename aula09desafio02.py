#numero = (input('Digite um número de 0 a 9999: '))
#numero.replace('', '000')
#print(f'unidade: {numero[3]}')
#print(f'dezena: {numero[2]}')
#print(f'centena: {numero[1]}')
#print(f'milhar: {numero[0]}')
#'jeito errado'

#'correção'
num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número {num}, podemos obter o seguinte resultado')
print(f'Ele possuí {u} unidades.')
print(f'Ele possuí {d} dezenas.')
print(f'Ele possuí {c} centenas.')
print(f'Ele possuí {m} milhares.')

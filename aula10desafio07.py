salario = float(input('Digite seu salário atual: '))
print(f'Seu atual salário é de: {salario:.2f}')
if salario > 1250:
    pc = salario + (10*salario)/100
    print(f'Você recebeu um aumento, seu novo salário é de: R${pc:.2f}')
if salario < 1250:
    pc = salario + (15*salario)/100
    print(f'Você recebeu um aumento, seu novo salário é de: R${pc:.2f}')

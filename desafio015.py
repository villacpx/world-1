print('Aluguel de carros')
d = int(input('Quantos dias você permaneceu com o carro? '))
km = float(input('Quantos kms foram percorridos? '))
da = (d*60)
kmr = (km*0.15)
print(f'o seu aluguel será de {float(da+kmr):.2f}')

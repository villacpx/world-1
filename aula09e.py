#'JUNÇÃO'
frase = 'Curso em vídeo Python'
print(frase.split())
print('-'.join(frase.split()))
print('ERRO 01    ', '-'.join(frase))
print('TESTE 01    ', ''.join(frase))
print('TESTE 02    ', ' '.join(frase))
print('TESTE 03    ', ''.join(frase.split()))
print('TESTE 04    ', ' '.join(frase.split()))
#'SEGUNDO MODO DE EXECUÇÃO'
divi = frase.split()
print('-'.join(divi))

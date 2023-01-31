frase = str(input('Digite sua frase: '))
a1 = frase.find('a')
a2 = frase.rfind('a')
print(f"""A primeira vez que apareceu a letra A em sua frase foi no caractere {a1},
e a última vez foi no {a2}!""")

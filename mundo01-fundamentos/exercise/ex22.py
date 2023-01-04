nome = str(input('Escreva seu nome completo: ')).strip()

print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))

div = nome.split()
print(len(div[0]))
## Texto grandes no print
# print("""Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
# Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
# when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
# It has survived not only five centuries, but also the leap into electronic typesetting, 
# remaining essentially unchanged. It was popularised in the 1960s with the release of 
# Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software 
# like Aldus PageMaker including versions of Lorem Ipsum.""")


frase = 'Curso em Vídeo Python'

##Posições
print(frase[::2])

## Transforma em maiusculas e conta quantos "O" tem 
print(frase.upper().count('O'))

## Conta o tamanho da frase e retira espaços
print(len(frase.strip()))

## Utilizando Replace
print(frase.replace('Python', 'Android'))

## Utilizando In
print('Curso' in frase)

##Utilizando Find
print(frase.lower().find('vídeo'))

## Utilizando split
dividido = frase.split()
print(dividido[2][3])
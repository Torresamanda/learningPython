n = input('Digite algo: ')
print('O tipo primitivo de valor é: ', type(n))

print('Só tem espaços? ', n.isspace())
print('É um número? ', n.isnumeric())
print('É alfabetico? ', n.isalpha())
print('É alfanumérico? ', n.isalnum())
print('Esta em Maiuscula? ', n.isupper())
print('Esta em minuscula? ', n.islower())
print('Esta capitaliza? ', n.istitle())



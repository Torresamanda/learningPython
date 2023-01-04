viagem = float(input('Qual a distância total da sua viagem? '))
print('Você está preste a começar uma viagem de {}Km.'.format(viagem))
if viagem <= 200:
    preco = viagem * 0.50
else:
    preco = viagem * 0.45

# preco = viagem * 0.50 if viagem <= 200 else viagem * 0.45

print('E o preço da sua passagem será de R${:.2f}'.format(preco))
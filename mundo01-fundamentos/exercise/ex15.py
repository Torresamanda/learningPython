n1 = float(input('Quantos dias foi alugado o carro? '))
n2 = float(input('Quantos km foi rodado o carro? '))
d = (n1 * 60) + ( n2 * 0.15)
print('O total a pagar é R${:.2f}'.format(d))
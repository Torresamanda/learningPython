salario = float(input('Qual salário do functionário? R$'))

if salario <= 1250:
    novo = salario + (salario * 15 / 100) 
else:
    novo = salario + (salario * 10 / 100)

print('Quem ganhava R${:.2f} passa a ganha {:.2f} agora.'.format(salario, novo))
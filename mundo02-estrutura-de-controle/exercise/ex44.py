print('{:=^40}'.format(' Lojas Amanda '))
preco = float(input('Preço das compras: R$'))
print('''
FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
''')

opcao = int(input('Qual é a opção? '))

if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcela em 2x de R${:.2f}, sem juros.'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcelada {}x de R${:.2f}, com juros.'.format(totalparc, parcela))
else:
    total = preco
    print('Opção inválida, tente novamente!')

print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
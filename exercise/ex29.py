car = float(input('Qual é a velocidade do carro? '))
if car > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    print('Você deve pagar uma multa de R${:.2f}'.format(( car - 80) * 7))
print('Tenha um bom dia! Dirija com segurança!')



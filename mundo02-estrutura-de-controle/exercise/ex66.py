num = soma = quant = 0

while True:
    num = int(input('Digite um número [digite 999 para parar]: '))
    if num == 999:
        break
    soma += num
    quant += 1

print('Você digitou {} e a soma deles é {}'.format(quant , soma))
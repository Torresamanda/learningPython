from random import randint
from time import sleep

pc = randint(0, 5)
print('-=-' * 10)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 10)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == pc:
    print('Você ganhou! Eu pensei no número {}'.format(pc))
else:
    print('Você perdeu! Eu pensei no número {}'.format(pc))


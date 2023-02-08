from random import randint
from time import sleep
from operator import itemgetter

jogadores = {'jogador1': randint(0, 6), 'jogador2': randint(0, 6), 'jogador3': randint(0, 6), 'jogador4': randint(0, 6)}

ranking = list()

print('Valores Sorteados: ')
for k, v in jogadores.items():
    print(f'{"O":>5} {k} tirou {v}')
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('=' * 30)

print('Ranking dos jogadores: ')
for i, v in enumerate(ranking):
    print(f'{i + 1:>5}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
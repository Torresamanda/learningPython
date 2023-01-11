times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo',
'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo',
'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')

print('-=' * 15)
print(f'Lista de times: {times}')
print('-=' * 15)

print(f'Os 5 primeiros são {times[:6]}')
print('-=' * 15)
print(f'Os 4 últimos times são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfábetica {sorted(times)}')
print('-=' * 15)
print(f'O Flamengo está na {times.index("Flamengo")+1}ª posição')
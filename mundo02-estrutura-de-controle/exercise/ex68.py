from random import randint

v = 0

while True:
    jogador = (int(input('Diga um valor: ')))
    pc = randint(0, 10)
    total = jogador + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar [P/I]? '))
    print(f'Você jogou {jogador} e o computador {pc}. Total de {total}. ', end='')
    print('Deu par!' if total % 2 == 0 else 'Deu Ímpar!')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print("Vamos jogar novamente...")
print(f'GAME OVER! Você venceu {v} vezes')
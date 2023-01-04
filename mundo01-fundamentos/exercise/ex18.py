import math

an = float(input('Digite o ângulo que você deseja calcular: '))

seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tan = math.tan(math.radians(an))

print('O seno do ângulo {} é {:.2f}'.format(an, seno))
print('O cosseno do ângulo {} é {:.2f}'.format(an, cosseno))
print('A tangente do ângulo {} é {:.2f}'.format(an, tan))

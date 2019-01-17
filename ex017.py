from math import hypot
from random import randint
b = randint(10, 15)
c = randint(10, 15)
print('Digite o cateto oposto: {}'.format(b))
print('Digite o cateto adjacente: {}'.format(c))
print('A hipotenusa é {:.2f}'.format(hypot(b, c)))

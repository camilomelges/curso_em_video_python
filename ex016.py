from math import trunc
from random import uniform
print('Digite um número: ')
n = uniform(10, 100)
print('O número {} tem a parte inteira {}'.format(n, trunc(n)))

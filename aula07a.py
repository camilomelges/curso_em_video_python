# + adição
# - subtração
# * multiplicação
# / divisão
# ** potencia
# // divisão inteira
# % resto

nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {0:^20}!'.format(nome))
print('Prazer em te conhecer {0:>20}!'.format(nome))
print('Prazer em te conhecer {0:=^20}!'.format(nome))
print('Prazer em te conhecer {0:=>20}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {0}.\nO produto é {1}.\nA divisão é {2:.3f}.'.format(s, m, d), end='\n')
print('Divisão inteira {} e potência {}'.format(di, e))
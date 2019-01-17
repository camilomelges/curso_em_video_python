from random import randint, choice
a1 = ['Rafael', 'Kennzo', 'Gaules', 'Claudia Chacha'];
a = randint(0, 3)

print('O aluno escolhido foi {}'.format(a1[a]))
print('O aluno escolhido foi {}'.format(choice(a1)))

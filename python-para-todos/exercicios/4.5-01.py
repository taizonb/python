'''
Exercício 1: Rode o programa anterior no seu computador para ver
quais números aparecem. Rode o programa mais uma vez e veja quais
números aparecem.
'''

import random

for i in range(3):
    x = random.random()
    print(x)

for i in range(3):
    x = random.randint(5,10)
    print(x)

t = [1, 2, 3, 4, 5, 6]
for i in range(3):
    x = random.choice(t)
    print(x)
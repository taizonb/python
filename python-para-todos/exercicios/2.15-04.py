'''
Exercício 4: Suponha que executamos as seguintes declaração por atribuição:
Largura = 17
Altura = 12.0

Para cada uma das expressões a seguir, escreva o valor da expressão e o tipo (do valor da expressão).
1. Largura//2
2. Largura/2.0
3. Altura/3
4. 1 + 2 * 5
'''



'''
Resposta:
1 - 17 (Integer)
2 - 8.5 (Float)
3 - 4 (Float)
4 - 11 (Integer)

'''

largura = 17
altura = 12.0

a = largura//2
b = largura/2.0
c = altura/3
d = 1+2*5

print(f'a = {a} {type(a)}\nb = {b} {type(b)}\nc = {c} {type(c)}\nd = {d} {type(d)}')
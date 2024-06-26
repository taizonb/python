'''
Exercício 2: Escreva um programa que procure por uma linha na forma:
Nova Revisão: 39772

Extraia o número de cada linha usando uma expressão regular e o método findall(). Compute o valor médio dos números e mostre-o.

Arquivo de entrada: mbox.txt
38444.0323119

Arquivo de entrada: mbox-short.txt
39756.9259259
'''


# Solução 01:

_arquivo = input('Arquivo de entrada: ')

teste = 0
while (teste == 0):
    try:
        arquivo = open(_arquivo, 'r')
        teste = 1
    except:
        print('Arquivo não encontrado.')
        teste = 0

print('agora foi!')
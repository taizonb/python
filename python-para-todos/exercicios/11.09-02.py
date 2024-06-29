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

import re


count = 0
sum = 0

# Abre o arquivo desejado:
teste = 0
_arquivo = input('Arquivo de entrada: ')
while (teste == 0):
    try:
        arquivo = open(_arquivo, 'r')
        teste = 1
    except:
        _arquivo = input('Arquivo não encontrado. Digite novamente: ')
        teste = 0


# Procura o termo na linha:
for linhas in arquivo:
    linhas = linhas.strip()
    termo = re.findall('^New Revision: ([0-9.]+)', linhas)
    
    if (len(termo) > 0):
        for val in termo:
            count += 1
            sum += float(val)
            print(f'Nova Revisão: {val}')


# Verifica se foram encontrados
if (count == 0):
    print('Não foram encontrados valores')
    exit
# Calcula a média dos valores e mostra na tela:
else:
    med = sum/count
    print(f'Média: {med}')
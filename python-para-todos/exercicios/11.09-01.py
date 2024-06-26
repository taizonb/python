'''
Exercício 1: Escreva um programa simples para simular a operação do comando grep em Unix. Peça ao usuário para entrar com uma expressão regular e conte o número de linhas que se igualam à expressão digitada:

$ python grep.py
Digite uma expressão regular: ^Autor
mbox.txt teve 1798 linhas que se igualam a ^Autor

$ python grep.py
Digite uma expressão regular: ^Xmbox.
txt teve 14368 linhas que se igualam a ^X-

$ python grep.py
Digite uma expressão regular: java$
mbox.txt teve 4175 linhas que se igualam a java$
'''


# Solução 01:

import re

contagem = 0
qtd = list()

_exp = input('Digite uma expressão regular: ')
arquivo = open('mbox-resumo.txt')

# Testa o que o usuário escreveu
try:
    exp = str(_exp)

except:
    print('Há algo de errado em sua expressão.')
    exit()

print(_exp)
# Itera para procurar a expressão nas linhas do arquivo
for linhas in arquivo:
    linhas = linhas.strip()

    # Opção com findall
    if (re.findall(exp, linhas) != []):
        contagem += len(re.findall(exp, linhas))


# Mostra a quantidade encontrada
print(contagem)
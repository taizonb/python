'''
Exercício 3: Escreva um programa que leia um registro de mensagens, construa um histograma, utilizando um dicionário, para contar quantas mensagens chegaram em cada endereço de email e mostre em tela o dicionário.

Enter a file name: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}
'''


# Solução 01:

import string

cont = dict()

'''' Testa a abertura do arquivo: '''
try:
    arquivo = open('mbox-short.txt')

except:
    print('Arquivo não encontrado.')
    exit()


for linhas in arquivo:
    linhas = linhas.rstrip()
    linhas = linhas.translate(linhas.maketrans('', '', string.punctuation))
    linhas = linhas.lower()
    palavras = linhas.split()

    if (len(palavras) < 2) or (palavras[0] != 'author'):
        continue

    if palavras[1] not in cont:
        cont[palavras[1]] = 1
    else:
        cont[palavras[1]] += 1

print(cont)
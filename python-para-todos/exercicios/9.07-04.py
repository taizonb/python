'''
Exercício 4: Adicione linhas de código no programa abaixo para identificar quem possui mais mensagens no arquivo. Após todo o dado ser
lido e todo o dicionário ser criado, procure no dicionário, utilizando um laço máximo (Veja o capítulo 5: Laços máximo e mínimo), quem tem o
maior número de mensagens e mostre em tela quantas mensagens essa pessoa tem.

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195
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


''' Coloca os dados em um dicionário: '''
for linhas in arquivo:
    linhas = linhas.rstrip()
    #linhas = linhas.translate(linhas.maketrans('', '', string.punctuation))
    linhas = linhas.lower()
    palavras = linhas.split()

    if (len(palavras) < 3) or (palavras[0] != 'from'):
        continue

    #cont[mail[1]] = palavras.get(mail[1].value, 1) + 1
    if palavras[1] not in cont:
        cont[palavras[1]] = 1
    else:
        cont[palavras[1]] += 1


''' procura a maior e menor qtd de e-mails: '''
maior = None
menor = None
for x, y in cont.items():
    if (maior is None) or (y > maior):
        maior = y
        maximo = x

    if (menor is None) or (y < menor):
        menor = y
        minimo = x


print(maximo, cont[maximo])
print(minimo, cont[minimo])
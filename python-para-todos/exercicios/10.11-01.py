'''
Exercício 1: Revise um programa anterior como é pedido: Leia e analise as linhas com “From” e retire os endereços dessas linhas. Conte o número de mensagens de cada pessoa usando um dicionário. Depois de todos os dados serem lidos, mostre a pessoa com mais envios criando uma lista de tuplas (contagem, email) do dicionário. Então, ordene a lista em ordem reversa e mostre a pessoa na primeira posição.

Linha simples:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
Digite o nome do arquivo: mbox-short.txt
cwen@iupui.edu 5

Digite o nome do arquivo: mbox.txt
zqian@umich.edu 195
'''


# Solução 01:

import string

mails = dict()
mails_lista = list()

# Abre o arquivo fonte
try:
    arquivo = open('mbox-short.txt', 'r')

except:
    print('Arquivo não encontrado.')


# Lê as linhas e coloca as palavras em uma lista
for linhas in arquivo:
    linhas = linhas.rstrip()
    linhas = linhas.lower()
    #linhas = linhas.translate(linhas.maketrans('', '', string.punctuation))
    palavras = linhas.split()

    # testa as linhas para ver se começam com 'from'
    if (len(palavras) < 4) or (palavras[0] != 'from'):
        continue

    # Cria o dicionário com os emails e conta
    if palavras[1] not in mails:
        mails[palavras[1]] = 1
    else:
        mails[palavras[1]] += 1

# cria uma lista de tuplas para inverter a chave-item
for mail, qtd in mails.items():
    mails_lista.append((qtd, mail))

# Ordena a lista de forma decrescente
mails_lista.sort(reverse=True)

# Print dos resultados
for qtd, mail in mails_lista:
    print(qtd, mail)

x, y = mails_lista[0]

print(f'Quem mais enviou e-mails foi: "{y}" com {x} mensagens')
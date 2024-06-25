'''
Exercício 2: Escreva um programa que categorize cada mensagem de e-mail de acordo com o dia em que a mensagem foi enviada. Para isso, procure por linhas que comecem com “From”, depois procure pela terceira palavra e mantenha uma contagem de ocorrência para cada dia da semana. No final do programa, mostre em tela o conteúdo do seu dicionário (a ordem não interessa).

linha exemplo:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

Exemplo de código:
python dow.py
Enter a file name: mbox-short.txt
{'Sex': 20, 'Qui': 6, 'Sab': 1}
'''


# Solução 01:

import string

semanas = dict()
arquivo = open('mbox-short.txt', 'r')

for linhas in arquivo:
    linhas = linhas.rstrip()
    linhas = linhas.translate(linhas.maketrans('','', string.punctuation))
    linhas = linhas.lower()
    palavras = linhas.split()

    #print(palavras)
    if (len(palavras) < 3) or (palavras[0] != 'from'):
        continue

    
    if (palavras[2] not in semanas):
        semanas[palavras[2]] = 1
    else:
        semanas[palavras[2]] += 1

print(semanas)
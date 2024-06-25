'''
Exercício 5: Esse programa grava o domínio de email (ao invés do endereço) de onde a mensagem foi enviada ao invés de quem o email veio (i.e., o endereço completo da mensagem). No final do programa, mostre em tela o conteúdo do seu dicionário.

python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
'''


# Solução 01:

import string

cont = dict()

try:
    arquivo = open('mbox-short.txt')

except:
    print('Arquivo não encontrado.')


''' Iteração para ler as linhas do documento '''
for linhas in arquivo:
    ''' Ajusta os valores das linhas para palavras '''
    linhas = linhas.rstrip()
    #linhas = linhas.translate(linhas.maketrans(string.punctuation))
    linhas = linhas.lower()
    palavras = linhas.split()

    ''' pula a iteração se não começar com from '''
    if (len(palavras) < 4) or (palavras[0] != 'from'):
        continue

    ''' Altera o valor do e-mail para apenas o domínio '''
    letra_cont = 0
    for letra in palavras[1]:
        letra_cont += 1
        if (letra == '@'): 
            break
    # Também poderia usar a built in "split()" para quebrar a palavra em duas a partir do @.
        
    palavra_aj = palavras[1]
    palavra_aj = palavra_aj[letra_cont:]

    ''' Adiciona no dicionário: '''
    if palavra_aj not in cont:
        cont[palavra_aj] = 1
    else:
        cont[palavra_aj] += 1


print(cont)
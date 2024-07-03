'''
Exercício 3: Use urllib para replicar o exercício anterior (1) recuperando um documento de uma URL, (2) mostrando até 3000 caracteres e (3) contando o total destes no documento. Não se preocupe sobre os cabeçalhos para esse exercício, apenas mostre os 3000 primeiros caracteres do contepudo do documento.

site teste: http://data.pr4e.org/romeo.txt
'''


# Solução 01:

import urllib.request, urllib.parse, urllib.error
import string


palavras_limite = 115   # Limites para qtd de palavras apresentadas
palavras_total = 0


# Pega o site digitado
_site = input('Digite o site que deseja: ')
#site = _site.split('/')  # pega somente o servidor
#site = site[2]

try:
    site = urllib.request.urlopen(_site)
    
    for linhas in site:
        linhas = linhas.decode().strip()

        if (palavras_total <= palavras_limite):

            print(linhas[:palavras_limite - palavras_total])

        palavras_total += len(linhas) 

except:
    print('Site digitado incorreto. ')


if (palavras_total > 1):
    print(f'\nQuantidade de caracteres mostrador: {palavras_limite}')
    print(f'Quantidade de caracteres totais: {palavras_total}')
'''
Exercício 4: Altere o programa urllinks.py para extrair e contar astags de parágrafos (p) do documento de HTML recuperado e mostrar a contagem dos parágrafos como uma saída do seu programa.Não mostre o conteúdo, apenas conte-os. Teste seu programa em várias páginas da web pequenas e também em algumas maiores.

site teste: http://data.pr4e.org/romeo.txt
'''


# Solução 01:

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


# Ignore SSL certificate erros
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Digite a URL que deseja: ')


try:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

except:
    print('Url digitada incorreta.')
    exit()


# Conta as TAGs de paragrafo "p"
count = 0

tags = soup('p')
for tag in tags:
    count += 1


# Exibe a quantidade de parágrafos
print(f'A quantidade de parágrafos foi de: {count}')
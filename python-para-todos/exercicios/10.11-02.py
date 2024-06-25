'''
Exercício 2: Esse programa conta a distribuição de horas no dia para cada uma das mensagens. Você pode retirar a hora da linha com “From” achando a string de horário e então separando ela em partes usando o caractere “:” (dois pontos). Uma vez acumuladas as contagens para cada hora, mostre os valores, um por linha, ordenados por hora como segue abaixo:

python timeofday.py
Digite o nome do arquivo: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
'''


# Solução 01:

import string

contador = dict()
contador_lista = list()

# Importar aquivo
try:
    arquivo = open('mbox-short.txt', 'r')
except:
    print('Arquivo não encontrado.')


# Lê as linhas do arquivo para colocar no BD
for linhas in arquivo:
    linhas = linhas.rstrip()
    #linhas = linhas.translate(linhas.maketrans('', '', string.punctuation))
    linhas = linhas.lower()
    palavras = linhas.split()

    # Condição para pegar somente as linhas que comecam com from
    if (len(palavras) < 6) or (palavras[0] != 'from'):
        continue
    
    # Arruma o formato da hora
    palavra_aj = palavras[5].split(':')

    # Pegar a data e quantidade de vezes que aparece o numero
    if palavra_aj[0] not in contador:
        contador[palavra_aj[0]] = 1
    else:
        contador[palavra_aj[0]] += 1


# Ordenar os valores por hora:
for hora, qtd in contador.items():
    contador_lista.append((hora, qtd))

contador_lista.sort()


# Mostra os valores na tela
for hora, qtd in contador_lista:
    print(hora, qtd)
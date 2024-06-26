'''
Exercício 3: Escreva um programa que leia um arquivo e mostre as letras em ordem decrescente de frequência. Seu programa deve converter todas as entradas para Caixa baixa e apenas contar as letras de a à z. Não conte espaços, dígitos, pontuações, ou qualquer coisa que não seja uma letra do alfabeto. Encontre textos simples de diversas línguas diferentes e veja como a frequência de letras varia entre os idiomas. Compare seis resultados com as tabelas em:

https://wikipedia.org/wiki/Letter_frequencies.
'''


# Solução 01:

import string

cont = dict()
cont_aj = list()

# Abre o arquivo desejado
_arquivo = input('Digite o arquivo que deseja comparar: ')

try:
    arquivo = open(_arquivo, 'r')

except:
    print('Arquiv não encontrado.')
    exit()


# Lê as linhas, retira o indesejado e coloca tudo em uma grande string
for linhas in arquivo:
    linhas = linhas.rstrip()
    linhas = linhas.translate(linhas.maketrans('', '', string.punctuation))
    linhas = linhas.translate(linhas.maketrans('', '', ))
    linhas = linhas.lower()

    # Condição para retirar linhas vazias
    if (len(linhas) == 0): continue

    # Iteração para contar apenas letras
    numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)   
    for letra in linhas:
        if letra not in numeros:
            if letra not in cont:
                cont[letra] = 1
            else:
                cont[letra] += 1

    for a in cont:
        print(cont)


    '''
    # Coloca o dicionário em uma lista para poder contar
    for x, y in cont.items():
        cont_aj.append((y, x))
    

    # Ordena a nova lista
    cont_aj.sort()

    # Mostra a lista na tela
    for x, y in cont_aj:
        print(y, x)

    '''
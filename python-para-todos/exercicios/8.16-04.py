'''
Exercicio 4: Baixe a copia do arquivo www.py4e.com/code3/romeo.txt.
Escreva um programa para abrir o arquivo chamado romeo.txt e leia-o linha por linha. Para cada linha, separe-a em uma lista de palavras usando a função split. Para cada palavra, cheque se esta palavra já existe na lista. Caso não exista, adicione ela. Quando o programa terminar de verificar, ordene e imprima estas palavras em ordem alfabética.**

Digite o nome do arquivo: romeo.txt
['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
'and', 'breaks', 'east', 'envious', 'fair', 'grief',
'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
'sun', 'the', 'through', 'what', 'window',
'with', 'yonder']
'''

# Solução 01:

lista_palavras = list()
arquivo = open('romeo.txt', 'r')


for linha in arquivo:
    linha = linha.split()

    for palavra in linha:
        if palavra not in lista_palavras:
            lista_palavras.append(palavra)


lista_palavras.sort()
print(lista_palavras)
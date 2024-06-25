'''
Exercício 1: Faça o download de uma cópia do arquivo

www.py4e.com/code3/words.txt

Escreva um programa que leia as palavras em words.txt e as armazena como chaves em um dicionário. Não importa quais são os valores. Então, você pode usar o operador in como uma maneira rápida de verificar se uma string está no dicionário.
'''


# Solução 01:

teste = 'um'
palavras = dict()
arquivo = open('words.txt', 'r')

for linha in arquivo:
    linha = linha.split()

    for palavra in linha:
        palavras[palavra] = 0

while (teste != 'fim'):
    teste = input('Digite uma palavra: ')
    if teste in palavras:
        print(f'A palavra "{teste}" está no arquivo "words.txt"')
    else:
        print(f'A palavra "{teste}" não está no arquivo "words.txt"')
'''
Exercício 3: Reescreva o código guardião nos exemplos acima sem duas declarações if. Em vez disso, use uma expressão lógica composta usando o operador lógico or, com uma única declaração if.

Utilize o arquivo: mbox-short-v2.txt
'''


# Solução 01:


arquivo = open('mbox-short-v2.txt', 'r')

for linha in arquivo:
    palavra = linha.split()
    if (len(palavra) == 0) or (len(palavra) < 3) or (palavra[0] != 'From'):
        continue
    print(palavra[2])
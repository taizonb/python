'''

Exercício 2: Descubra qual linha do programa abaixo não está devidamente protegida. Veja se você pode construir um arquivo de texto que causa falha no programa e depois modifique o programa para que a
linha seja propriamente protegida e por fim, teste o programa para ter certeza que ele manipula corretamente o novo arquivo de texto.

arquivo: 08.14.txt

fhand = open('mbox-short.txt')
contador = 0
for linha in fhand:
    palavras = line.split()
    # print 'Debug:', palavras
    if len(palavras) == 0 : continue
    if palavras[0] != 'De' : continue
    print(palavras[2])
'''

# Solução01 - Pode haver a palavra From começando uma linha e o resultado ser diferente do esperado.

fhand = open('mbox-short-v2.txt')
contador = 0
for linha in fhand:
    palavras = linha.split()
    #print('Debug:', palavras)
    if (len(palavras) == 0) or (len(palavras) < 3) or (palavras[0] != 'From') : continue
    print(palavras[2])
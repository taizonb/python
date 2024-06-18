'''
Exercício 1: Escreva um loop while que inicia no último caractere da string e caminha para o primeiro caractere, imprimindo cada letra em uma linha separada.
'''

# Solução 01:

_palavra = input('Digite uma palavra: ')

cont = len(_palavra)
while (cont > 0):
    letra = _palavra[cont-1]
    print(letra)
    cont = cont - 1
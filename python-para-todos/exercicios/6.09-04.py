'''
Exercício 4: Existe um método na string chamado count que é similar à função usada no exercício anterior. Leia a documentação desse método em:

https://docs.python.org/library/stdtypes.html#string-methods

Escreva uma invocação que conta o número de vezes que a letra “a” aparece em “banana”.**
'''

# Solução 01:

_palavra = input('Digite a palavra desejada: ')
_letra = input('Digite a letra que deseja procurar: ')

contagem = _palavra.count(_letra)

print(f'A letra "{_letra}" aparece {contagem} vez(es) na palavra "{_palavra}"')
'''
palavra = 'banana'
contagem = 0
for letra in palavra:
    if letra == 'a':
        contagem = contagem + 1
print(contagem)

Exercício 3: Encapsule esse código em uma função chamada contagem, e generalize para que ela aceite a string e a letra como argumentos.
'''

# Solução 01:

contagem = 0

_palavra = input('Digite a palavra que deseja: ')
_letra = input('Digite a letra que deseja contar: ')

for letra in _palavra:
    if letra == _letra:
        contagem = contagem + 1

print(f'A letra "{_letra}" aparece {contagem} veze(s) na palavra "{_palavra}"')
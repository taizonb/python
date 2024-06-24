'''
Exercício 6: Reescreva o programa que solicita o usuário uma lista de números e prints e imprime em tela o maior número e o menor número quando o usuário digitar a palavra “feito”. Escreva um programa para armazenar as entradas do usuário em uma lista e use as funções max() e min() para computar o número máximo e o mínimo depois que o laço for completo.

Digite um número: 6
Digite um número: 2
Digite um número: 9
Digite um número: 3
Digite um número: 5
Digite um número: feito
Máximo: 9.0
Mínimo: 2.0
'''

# Solução 01:

numeros_lista = list()

while True:
    _numero = input('Digite um número: ')

    try:
        numero = float(_numero)
        numeros_lista.append(numero)

    except:
        if (_numero == 'feito'):
            break
        else:
            print(f'Valor digitado "{_numero}" não é um número.')

maximo = max(numeros_lista)
minimo = min(numeros_lista)

print(f'Máximo: {maximo}')
print(f'Mínimo: {minimo}')
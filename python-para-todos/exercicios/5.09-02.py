'''
Digite um número: 4
Digite um número: 5
Digite um número: dado errado
Entrada Inválida
Digite um número: 7
Digite um número: pronto
16 3 5.333333333333333

Exercício 2: Escreva outro programa que pede por uma lista de números como mostrada acima e mostra, no final, o máximo e o mínimo dos números ao invés da média.
'''

# Solução 01:

num = None
num_qtd = None

while True:
    _num = input('Digite um número: ')

    try:
        num = int(_num)

        if (num_qtd == None):
            num_qtd = 1
        else:
            num_qtd = num_qtd + 1

        if (num_qtd == 1):
            maximo = num
            minimo = num
        else:
            if (num > maximo):
                maximo = num
            if (num < minimo):
                minimo = num

        print(f'Máximo: {maximo} / Mínimo: {minimo}.')

    except:
        if (_num == 'pronto'):
            break
        else:
            print('Digite um número inteiro válido')
        

# Mostra o máximo
print(f'Máximo valor: {maximo}')

# Mostra o mínimo
print(f'Mínimo valor: {minimo}')
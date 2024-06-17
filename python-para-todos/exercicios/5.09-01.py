'''
Exercício 1: Escreva um programa que lê repetitivamente números até que o usuário digite “pronto”. Quando “pronto” for digitado, mostre a soma total, a quantidade e a média dos números digitados. Se o usuário digitar qualquer coisa que não seja um número, detecte o erro usando o try e o except e mostre na tela uma mensagem de erro e pule para o próximo número.
'''

num_qtd = None
num_soma = None


while True:
    _num = input('Digite um número: ')

    try:
        num = int(_num)
        if (num_qtd is None):
            num_qtd = 1         
            num_soma = num
        else:
            num_qtd = num_qtd + 1      
            num_soma = num_soma + num     

    except:
        if (_num == 'pronto'):
            break
        else:
            print('Número inválido. Favor digitar somente inteiros.')


if (num_qtd is None):
    num_media = None
else:   
    num_media = num_soma/ num_qtd

# Soma dos números
print(f'Soma total: {num_soma}')

# Quantidade de números
print(f'Quantidade de números: {num_qtd}')

# Média dos números
print(f'Média dos números: {num_media}')
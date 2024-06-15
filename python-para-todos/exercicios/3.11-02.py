'''
Exercício 2: Reescreva seu programa de pagamento utilizando try e except, de forma que o programa consiga lidar com entradas não numéricas graciosamente, mostrando uma mensagem e saindo do programa. A seguir é mostrado duas execuções do programa
'''

# Programa de pagamento:
'''
Reescreva seu programa de pagamento, para pagar ao funcionário 1.5 vezes o valor da taxa horária de pagamento pelo tempo trabalhado acima de 40 horas

Escreva um programa que solicite ao usuário as horas e o valor da taxa por horas para calcular o valor a ser pago por horas de serviço.

Digite as Horas: 45
Digite a taxa: 10
Pagamento: 475.0
'''

# Solução 01:

horas = input(f'Digite as horas: ')
taxa = input(f'Digite a taxa: ')

try:
    horas_aj = int(horas)
    taxa_aj = float(taxa)

    if (horas_aj > 40):
        pagamento = horas_aj * (taxa_aj*1.5)

    else:
        pagamento = horas_aj * taxa_aj

    print(f'Pagamento: {pagamento}')

except:
    print('Digite as horas como inteiro e taxa como float')






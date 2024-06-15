'''
Exercício 1: Reescreva seu programa de pagamento, para pagar ao funcionário 1.5 vezes o valor da taxa horária de pagamento pelo tempo trabalhado acima de 40 horas

Escreva um programa que solicite ao usuário as horas e o valor da taxa por horas para calcular o valor a ser pago por horas de serviço.

Digite as Horas: 45
Digite a taxa: 10
Pagamento: 475.0
'''

#Solução 01

horas = int(input(f'Digite as horas: '))
taxa = float(input(f'Digite a taxa: '))

if (horas > 40):
    pagamento = horas * (taxa*1.5)
    
else:
    pagamento = horas * taxa

print(f'Pagamento: {pagamento}')

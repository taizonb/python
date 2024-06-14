""" 
Exercício 3: Escreva um programa que solicite ao usuário as horas e o
valor da taxa por horas para calcular o valor a ser pago por horas de
serviço.
"""

horas = int(input('Digite as horas: '))
taxa = float(input('Digite a taxa: '))

valor_pago = horas * taxa

print(f'Valor a ser pago: {valor_pago}.')
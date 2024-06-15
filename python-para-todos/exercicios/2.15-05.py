'''
Exercício 5: Escreva um programa que solicite ao usuário uma temperatura Celsius, converta para Fahrenheit, e mostre a temperatura convertida.
'''



# Solução 01:
'''
temp_celcius = float(input('Digite a temperatura em °C: '))
temp_fahrenheit = (temp_celcius*1.8) + 32
print(f'A temperatura em ºFahrenheit é: {temp_fahrenheit}')
'''


# Solução 02:

inp = input('Digite a temperatura em °C: ')
try:
    temp_celcius = float(inp)
    temp_fahrenheit = (temp_celcius*1.8) + 32
    print(f'A temperatura em ºFahrenheit é: {temp_fahrenheit}')
    
except:
    print('Digite a temperatura usando números e "."')

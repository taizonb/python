'''
Exercício 5: Utilize o seguinte código em Python que guarda uma string:

str = 'X-DSPAM-Confidence:0.8475'

Use a função find e o fatiamento de strings para extrair a porção da string depois do sinal de dois pontos e use a função float para converter a string extraída em um número de ponto flutuante.
'''


# Solução 01:

str = 'X-DSPAM-Confidence:0.8475'

fat_inic = str.find(':')
str_ajust = str[fat_inic+1:]

str_float = float(str_ajust)

print(str_float)
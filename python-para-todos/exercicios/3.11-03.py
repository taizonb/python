'''
Exercício 3: Escreva um programa que peça por uma pontuação entre 0.0 e 1.0. Se a pontuação for fora do intervalo, mostre uma mensagem de erro. Se a pontuação estiver entre 0.0 e 1.0, mostre a respectiva nota usando a seguinte tabela

Pontuação Nota
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F

'''

# Solução 01:

pontuacao = input('Digite uma pontuação entre 0.0 e 1.0: ')

try:
    pontuazao_aj = float(pontuacao)
    if (pontuazao_aj >= 0.9) and (pontuazao_aj <= 1.0):
        nota = 'A'
    elif (pontuazao_aj >= 0.8) and (pontuazao_aj <= 0.9):
        nota = 'B'
    elif (pontuazao_aj >= 0.7) and (pontuazao_aj <= 0.8):
        nota = 'C'
    elif (pontuazao_aj >= 0.6) and (pontuazao_aj <= 0.7):
        nota = 'D'
    elif (pontuazao_aj <= 0.6):
        nota = 'F'

    print(f'Nota: {nota}')

except:
    print('Digite um número válido.')
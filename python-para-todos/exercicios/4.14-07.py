'''
Exercício 7: Reescreva o programa de notas do capítulo anterior usando a função computarNotas que recebe a pontuação como parâmetro e retorna a nota como uma string.

Pontuação  Nota
 >= 0.9     A
 >= 0.8     B
 >= 0.7     C
 >= 0.6     D
  < 0.6     F
'''

def computarNotas(pontuacao):
    if (pontuacao >= 0.9) and (pontuacao <= 1.0):
        nota = 'A'
    elif (pontuacao >= 0.8) and (pontuacao < 0.9):
        nota = 'B'
    elif (pontuacao >= 0.7) and (pontuacao < 0.8):
        nota = 'C'
    elif (pontuacao >= 0.6) and (pontuacao < 0.7):
        nota = 'D'
    elif (pontuacao >= 0.0) and (pontuacao < 0.6):
        nota = 'F'
    return nota

inp_pontuacao = input('Insira a pontuação: ')

try:
    pontuacao = float(inp_pontuacao)
    if (pontuacao <= 1.0) and (pontuacao >= 0.0):
        nota = computarNotas(pontuacao)
        print(f'Nota: {nota}')
    else:
        print('Digite um valor entre 0.0 e 1.0')
except:
    print('Digite uma pontuação de 0.0 a 1.0.')
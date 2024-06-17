'''
Exercício 3: Mova a chamada da função de volta ao final e mova a definição de print_lyrics para depois da definição de repeat_lyrics. O que acontece quando você executa esse programa?

def print_LetraDeMusica():
    print("Eu sou um lenhador, e eu estou bem.")
    print('Eu durmo a noite toda e trabalho o dia todo.')

def repetir_LetraDeMusica():
    print_ LetraDeMusica()
    print_ LetraDeMusica()   

repetir_LetraDeMusica() 
'''


#Solução 01:

def repetir_LetraDeMusica():
    print_LetraDeMusica()
    print_LetraDeMusica() 

def print_LetraDeMusica():
    print("Eu sou um lenhador, e eu estou bem.")
    print('Eu durmo a noite toda e trabalho o dia todo.')    

repetir_LetraDeMusica()


# Resposta:
# O programa segui corretamente, pois as funções ficaram na memória do computador.
'''
Exercício 2: Mova a última linha desse programa para o início, assim a
chamada da função aparece antes das definições. Execute o programa e
veja qual mensagem de erro aparece.

def print_LetraDeMusica():
    print("Eu sou um lenhador, e eu estou bem.")
    print('Eu durmo a noite toda e trabalho o dia todo.')

def repetir_LetraDeMusica():
    print_ LetraDeMusica()
    print_ LetraDeMusica()   

repetir_LetraDeMusica() 
'''


#Solução 01:

'''repetir_LetraDeMusica() 

def print_LetraDeMusica():
    print("Eu sou um lenhador, e eu estou bem.")
    print('Eu durmo a noite toda e trabalho o dia todo.')

def repetir_LetraDeMusica():
    print_LetraDeMusica()
    print_LetraDeMusica() 

'''  


# Resposta:
# NameError: name 'repetir_LetraDeMusica' is not defined
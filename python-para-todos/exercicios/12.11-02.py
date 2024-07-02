'''
Exercício 2: Altere seu programa de soquete para que ele conte o número de caracteres que recebeu e pare de mostrar qualquer texto depois que mostrar 3000 caracteres. O programa deve recuperar o documento inteiro e contar o número total de caracteres e mostrar o resultado da contagem no final do documento.

site teste: http://data.pr4e.org/romeo.txt
'''


# Solução 01:

import socket

_url = input('Digite uma URL: ')
count = 0


mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_url = _url.split('/')   # Quebra o endereço todo na URL simples

try:
    mysock.connect((host_url[2], 80))   # Conecta ao servidor
    cmd = f'GET {_url} HTTP/1.0\r\n\r\n'.encode()   # Ajusta a url no padrão
    mysock.send(cmd)   # Envia a URL ajustadapara para o servidor
    data = mysock.recv(510)   # Recebe os primeiros "X" caracteres
    print(data.decode(),end='')

    count += len(data)   # Conta a qtd de caracteres total

    while (len(data) > 1):
        data = mysock.recv(510)   # Loop que recebe o restante dos caracteres
        count += len(data)   # Conta a qtd de caracteres total
        mysock.close()

# Caso de errado, sai do loop e fecha o programa
except:
    print('URL digitada incorreta.')


# Mostra as informações na tela e conta o total de caracteres
if (count != 0):
    print(f'\nQuantidade de caracteres: {count}')
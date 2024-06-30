'''
Exercício 2: Altere seu programa de soquete para que ele conte o número de caracteres que recebeu e pare de mostrar qualquer texto depois que mostrar 3000 caracteres. O programa deve recuperar o documento inteiro e contar o número total de caracteres e mostrar o resultado da contagem no final do documento.
'''


# Solução 01:

import socket

_url = input('Digite uma URL: ')
count = 0

try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host_url = _url.split('/')

    print(host_url[2])

    mysock.connect((host_url[2], 80))
    cmd = f'GET {_url} HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        count += count + len(data)
        print(data.decode(),end='')
        mysock.close()

except:
    print('URL digitada incorreta.')


print(f'\nQuantidade de caracteres: {count}')
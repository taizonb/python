'''
Exercício 1: Altere o programa de soquete socket1.py pR pedir ao usuário a URL para que então possa ler qualquer página da web.Você pode usar split('/') para quebrar a URL em suas componentes para que então possa extrair o nome do hospedeiro para que o soquete connect chame. Adicione tratamento de erro usando try e except para lidar com a condição do usuário digitar uma URL formatada incorretamente ou uma não existente

site teste: http://data.pr4e.org/romeo.txt
'''


# Solução 01:

import socket

# Importando a URL
_url = input('Digite uma URL: ')
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_url = _url.split('/')   # Quebra a URL para o dominio
mysock.connect((host_url[2], 80))
cmd = f'GET {_url} HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)


while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
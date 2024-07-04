'''
Exercício 5: (Avançado) Altere o programa de soquete para que ele apenas mostre uma informação depois dos cabeçalhos e uma linha em branco ser recebida. Lembre que recv recebe caracteres (newlines e etc), não linhas.

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
data = mysock.recv(512)

# Procura o final do cabeçalho
message = data.decode()
header_finish = message.find('\n')

print(message)
'''
Exercício 2: Às vezes, quando os programadores estão entediados ou querem um pouco de diversão, eles adicionam um Easter Egg inofensivo em seus programas. Modifique o programa que solicita um arquivo ao usuário para que ele mostre uma mensagem engraçada quando o usuário deigitar no nome do arquivo “na na boo boo”. O programa deve se comportar normalmente para todos os outros arquivos que existem e que não existem. Aqui está uma amostra da execução desse programa:

python egg.py
Digite o nome de um arquivo: mbox.txt
Há 1797 linhas de assunto em mbox.txt

python egg.py
Digite o nome de um arquivo: missing.tyxt
Arquivo não pôde ser aberto: missing.tyxt

python egg.py
Digite o nome de um arquivo: na na boo boo
NA NA BOO BOO PRA VOCÊ TAMBÉM!

Você pode baixar o arquivo em: www.py4e.com/code3/mbox-short.txt
'''


# Solução 01:

cont = 0

_file = input('Digite o nome de um arquivo: ')

if (_file.lower() == 'na na boo boo'):
    print('NA NA BOO BOO PRA VOCÊ TAMBÉM!')
else:
    try:
        file = open(_file, 'r')
        
        for linhas in file:
            cont = cont + 1

    except:
        print('Arquivo não encontrado.')
        exit

if (cont > 0):
    print(f'Há {cont} linhas de assuntos em {_file}')        



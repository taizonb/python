'''
Exercício 1: Escreva um programa que leia um arquivo e mostre o conteúdo deste (linha por linha), completamente em caixa alta. A execução do programa deverá ser a seguinte: 

python shout.py
Digite o nome de um arquivo: mbox-short.txt

FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN 5 09:14:16 2008
RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
SAT, 05 JAN 2008 09:14:16 -0500

Você pode baixar o arquivo em: www.py4e.com/code3/mbox-short.txt

'''

# Solução 01:

_file = input('Digite o nome de um arquivo: ')


try:
    file = open(_file)

    for linha in file:
        linha = linha.rstrip().upper()
        print(linha)

except:
    print('Arquivo não encontrado.')
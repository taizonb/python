'''
Exercício 5: Escreva um programa que leia uma caixa de email, e quando você encontrar uma linha que comece com “De”, você vai separar a linha em palavras usando a função split. Nós estamos interessados em quem envia a mensagem, que é a segunda palavra na linha que começa com From.

De stephen.marquard@uct.ac.za Sáb Jan 5 09:14:16 2008

Você vai analisar a linha que começa com From e irá pôr para imprimir na tela a segunda palavra (para cada linha do tipo), depois o programa também deverá contar o número de linhas que começam com “De” e imprimir em tela o valor final desse contador. Esse é um bom exemplo da saída com algumas linhas removidas:

python fromcount.py
Digite o nome do arquivo: mbox-short.txt
stephen.marquard@uct.ac.za
louis@media.berkeley.edu
zqian@umich.edu

[...some output removed...]

ray@media.berkeley.edu
cwen@iupui.edu
cwen@iupui.edu
cwen@iupui.edu
There were 27 lines in the file with From as the first word


'''
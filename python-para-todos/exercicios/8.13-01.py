'''
Exercício 1: Escreva uma função chamada corte que recebe uma lista e a modifica, removendo o primeiro e o último elemento, e retorna None. Depois escreva uma função chamada meio que recebe uma lista e retorna uma nova lista que contém todos, menos o primeiro e o último elemento.
'''

###########################
##                       ##
##       Solução 01:     ##
##                       ##
###########################

# Funções:
def corte(conjunto_corte, n):
    conjunto_corte.pop(n-1)
    conjunto_corte.pop(0)
    return None

def meio(conjunto_meio, n):
    nova_lista = conjunto_meio[1:n-1]
    return nova_lista


# Argumentos
lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [1, 2, 3, 4, 5, 6]
cont = len(lista1)


# Chamada das funções
nova_lista1 = corte(lista1, cont)
nova_lista2 = meio(lista2, cont)


# Resultados
print(f'Quantidade de itens do objeto: {cont}')

print(f'lista1: {lista1}')
print(f'Nova Lista 1: {nova_lista1}')

print(f'Lista2: {lista2}')
print(f'Nova Lista 2: {nova_lista2}')

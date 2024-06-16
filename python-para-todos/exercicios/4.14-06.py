'''
Exercício 6: Reescreva seu programa de cálculo de pagamento com um 1.5 o valor de hora de trabalho por hora extra, crie uma função chamada calculoPagamento que aceita dois parâmetros(horas e TaxaHora).

Insira as Horas: 45
Insira o valor da Hora de Trabalho: 10
pagamento: 475.0
'''

def calculoPagamento(horas, TaxaHora):
    if (horas > 40):
        pagamento = horas*(TaxaHora*1.5)
    else:
        pagamento = horas*TaxaHora      
    return pagamento

inp_horas = input('Insira as Horas: ')
inp_taxa = input('Insira o valor da Hora de Trabalho: ')

try:
    horas_aj = int(inp_horas)
    taxa_aj = float(inp_taxa)
    pagamento = calculoPagamento(horas_aj, taxa_aj)
    print(f'pagamento: {pagamento}')

except:
    print('Digite as horas em inteiro e a taxa como float.')
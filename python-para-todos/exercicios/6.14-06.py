'''
Exercícios 6: Leia a documentação dos métodos da string em https://docs.python.org/library/stdtypes.html#string-methods
Você pode querer experimentar alguns deles para ter certeza que você entendeu como eles funcionam. strip e replace são particularmente úteis.
'''


# Solução 01:

# Strip:
x = '   teste   '
y = '.,; teste ;.,'

a = x.strip()
b = y.strip(' .,;')

print(a)
print(b)



# Replace:
x = 'Meu nome é Paty'

y = x.replace('Paty', 'Taizo')

print(x)
print(y)
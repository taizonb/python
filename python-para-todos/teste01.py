
'''
x = [3, 41, 12, 9, 74, 15]
maximo = None
print(f'Antes = {maximo}')

for num in x:
    if (maximo is None) or (maximo < num):
        maximo = num
    print(f'Laço = {num} / Máximo = {maximo}')


print(f'Máximo = {maximo}')
'''

fname = input('Enter the file name: ')

try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)
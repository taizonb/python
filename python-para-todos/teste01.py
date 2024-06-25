
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

'''fname = input('Enter the file name: ')

try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)'''

import string

fhand = open('romeo.txt')
counts = dict()

for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()

    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

# Sort the dictionary by value
lst = list()
for key, val in counts.items():
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[:10]:
    print(key, val)
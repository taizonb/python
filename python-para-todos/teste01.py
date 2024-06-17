
x = [3, 41, 12, 9, 74, 15]
maximo = None
print(f'Antes = {maximo}')

for num in x:
    if (maximo is None) or (maximo < num):
        maximo = num
    print(f'Laço = {num} / Máximo = {maximo}')


print(f'Máximo = {maximo}')
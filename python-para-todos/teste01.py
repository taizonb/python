while True:
    line = input('>')
    if line[0] == '#':
        continue
    if line == 'pronto':
        break
    print(line)

print('Pronto!')
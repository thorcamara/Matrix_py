matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
evensSum = greater = colSum = 0
for r in range(0, 3):
    for c in range(0, 3):
        matrix[r][c] = int(input(f'Type a number for [{r}, {c}]: '))
print('-=' * 30)
for r in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[r][c]:^5}]', end='')
        if matrix[r][c] % 2 == 0:
            evensSum += matrix[r][c]
    print()
print('-=' * 30)
print(f'The \033[4;33mSUM\033[m of the \033[4;31mEVEN\033[m numbers = \033[4;32m{evensSum}\033[m.')
for r in range(0, 3):
    colSum += matrix[r][2]
print(f'The \033[4;33mSUM\033[m of the numbers of the \033[4;34mTHIRD\033[m column = \033[4;32m{colSum}\033[m.')
for c in range(0, 3):
    if c == 0:
        greater = matrix[1][c]
    elif matrix[1][c] > greater:
        greater = matrix[1][c]
print(f'The GREATEST number of the \033[4;35mSECOND\033[m row = \033[4;32m{greater}\033[m.')

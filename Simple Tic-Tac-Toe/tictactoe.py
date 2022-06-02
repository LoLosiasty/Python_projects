grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
print('---------')
print(f'| {grid[0][0]} {grid[0][1]} {grid[0][2]} |')
print(f'| {grid[1][0]} {grid[1][1]} {grid[1][2]} |')
print(f'| {grid[2][0]} {grid[2][1]} {grid[2][2]} |')
print('---------')
turn = 'O'
while True:
    if turn == 'O':
        turn = 'X'
    else:
        turn = 'O'
    move = input().split()
    try:
        x = int(move[0]) - 1
        y = int(move[1]) - 1
        print(x, y)
    except TypeError:
        print("You should enter numbers!")
        continue
    if x not in [0, 1, 2] or y not in [0, 1, 2]:
        print("Coordinates should be from 1 to 3!")
        continue
    elif grid[x][y] != ' ':
        print('This cell is occupied! Choose another one!')
        continue
    else:
        grid[x][y] = turn
        print('---------')
        print(f'| {grid[0][0]} {grid[0][1]} {grid[0][2]} |')
        print(f'| {grid[1][0]} {grid[1][1]} {grid[1][2]} |')
        print(f'| {grid[2][0]} {grid[2][1]} {grid[2][2]} |')
        print('---------')
    if turn == grid[0][0] == grid[0][1] == grid[0][2]\
       or turn == grid[1][0] == grid[1][1] == grid[1][2]\
       or turn == grid[2][0] == grid[2][1] == grid[2][2]\
       or turn == grid[0][0] == grid[1][0] == grid[2][0]\
       or turn == grid[0][1] == grid[1][1] == grid[2][1]\
       or turn == grid[0][2] == grid[1][2] == grid[2][2]\
       or turn == grid[0][0] == grid[1][1] == grid[2][2]\
       or turn == grid[0][2] == grid[1][1] == grid[2][0]:
        print(turn, "wins")
        exit()
    if ' ' not in ''.join(grid[0]+grid[1]+grid[2]):
        print("Draw")
        exit()

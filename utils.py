import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_map(map, helicopter_pos):
    for row in range(len(map)):
        for col in range(len(map[0])):
            if (row, col) == helicopter_pos:
                print('🚁', end=' ')  # Вертолет
            elif map[row][col] == 'T':
                print('🌳', end=' ')  # Дерево
            elif map[row][col] == 'F':
                print('🔥', end=' ')  # Пожар
            elif map[row][col] == 'R':
                print('💧', end=' ')  # Вода
            else:
                print('🟩', end=' ')  # Пустая земля
        print()
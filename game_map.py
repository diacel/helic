import random

# Глобальные переменные
map_size = (10, 10)  # Размер карты
map = []  # Игровая карта

def initialize_map():
    global map
    map = [[' ' for _ in range(map_size[1])] for _ in range(map_size[0])]
    # Добавление деревьев и рек
    for row in range(map_size[0]):
        for col in range(map_size[1]):
            if random.random() < 0.2:  # 20% вероятность дерева
                map[row][col] = 'T'
            elif random.random() < 0.1:  # 10% вероятность реки
                map[row][col] = 'R'

def update_map():
    # Логика роста и возгорания деревьев
    for row in range(map_size[0]):
        for col in range(map_size[1]):
            if map[row][col] == 'T' and random.random() < 0.05:  # 5% вероятность возгорания
                map[row][col] = 'F'  # Пожар

def is_tree(row, col):
    return map[row][col] == 'T'

def is_fire(row, col):
    return map[row][col] == 'F'

def is_water(row, col):
    return map[row][col] == 'R'

def extinguish_fire(row, col):
    if map[row][col] == 'F':
        map[row][col] = 'T'  # Потушить пожар, остается дерево
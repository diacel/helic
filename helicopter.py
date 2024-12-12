import game_map
import score

# Глобальные переменные
position = (0, 0)  # Положение вертолета
water_tank = 1  # Количество воды в резервуаре
lives = 3  # Количество жизней

def initialize_helicopter():
    global position, water_tank, lives
    position = (0, 0)
    water_tank = 1
    lives = 3

def move(direction):
    global position
    row, col = position
    if direction == 'w' and row > 0:
        row -= 1
    elif direction == 's' and row < 9:
        row += 1
    elif direction == 'a' and col > 0:
        col -= 1
    elif direction == 'd' and col < 9:
        col += 1
    position = (row, col)

    # Автоматически забираем воду, если находимся над рекой
    if game_map.is_water(row, col):
        refill_water()

def refill_water():
    global water_tank
    water_tank = 1  # Пополнение резервуара

def extinguish_fire():
    global water_tank
    if water_tank > 0:
        water_tank -= 1
        return True
    return False

def update_helicopter():
    global lives
    # Проверяем, есть ли пожар под вертолетом
    row, col = position
    if game_map.is_fire(row, col):
        if extinguish_fire():  # Если удалось потушить пожар
            game_map.extinguish_fire(row, col)
            score.add_points(10)  # Добавляем 10 очков за тушение
        else:  # Если не удалось потушить пожар
            lives -= 1  # Вертолет теряет жизнь
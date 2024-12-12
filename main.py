import game_map
import helicopter
import weather
import hospital
import shop
import score
import utils

def main():
    print("Добро пожаловать в игру 'Пожарный вертолет'!")
    # Инициализация игровых объектов
    game_map.initialize_map()
    helicopter.initialize_helicopter()
    weather.initialize_weather()

    while True:
        utils.clear_screen()  # Очистка экрана
        game_map.update_map()  # Обновление карты
        helicopter.update_helicopter()  # Обновление вертолета
        weather.update_weather()  # Обновление погоды
        score.update_score()  # Обновление очков

        # Отрисовка карты
        utils.draw_map(game_map.map, helicopter.position)
        print(f"Очки: {score.points} | Жизни: {helicopter.lives} | Вода: {helicopter.water_tank}")

        # Ввод действия игрока
        action = input("Введите действие (w/a/s/d - перемещение, h - больница, u - магазин, q - выход): ").lower()
        if action == 'q':
            break
        elif action == 'h':  # Посещение больницы
            hospital.heal_helicopter()
        elif action == 'u':  # Посещение магазина
            shop.upgrade_water_tank()
        else:
            helicopter.move(action)

        # Проверка условий завершения игры
        if helicopter.lives <= 0:
            print("Игра окончена! Вы проиграли. 😢")
            break

if __name__ == "__main__":
    main()
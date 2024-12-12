import helicopter
import score

def upgrade_water_tank():
    """
    Увеличивает вместимость резервуара для воды, если у игрока достаточно очков.
    """
    if score.points >= 100:  # Требуется 100 очков для улучшения
        helicopter.water_tank += 1  # Увеличиваем вместимость резервуара
        score.points -= 100  # Снимаем очки
        print("🛒 Резервуар для воды улучшен! Теперь вместимость:", helicopter.water_tank)
    else:
        print("🛒 Недостаточно очков для улучшения резервуара.")
import helicopter
import score

def heal_helicopter():
    """
    Восстанавливает жизнь вертолету, если у игрока достаточно очков.
    """
    if helicopter.lives < 3 and score.points >= 50:  # Требуется 50 очков для восстановления жизни
        helicopter.lives += 1  # Восстанавливаем жизнь
        score.points -= 50  # Снимаем очки
        print("🏥 Вертолет восстановил жизнь!")
    elif helicopter.lives >= 3:
        print("🏥 У вертолета уже максимальное количество жизней.")
    else:
        print("🏥 Недостаточно очков для восстановления жизни.")
import random

weather_condition = "clear"

def initialize_weather():
    global weather_condition
    weather_condition = "clear"

def update_weather():
    global weather_condition
    if random.random() < 0.05:  # 5% вероятность изменения погоды
        weather_condition = random.choice(["rain", "wind", "clear"])
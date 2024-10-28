from workout_plan_generator import generate_workout_plan
from toJson import toJson
import json

workout_type = "Сплит"
days = ["Понедельник", "Среда" ,"Пятница"]
target_muscles = ["Руки", "Спина", "Грудь"]
difficulty = "Сложный"
conditions = "Спортивный зал"


json_workout_plan = toJson(generate_workout_plan(workout_type=workout_type,
                                                 days=days,
                                                 target_muscles=target_muscles,
                                                 difficulty=difficulty,
                                                 conditions=conditions))

with open('workout_program.json', 'w', encoding='utf-8') as f:
    json.dump(json_workout_plan, f, ensure_ascii=False, indent=4)
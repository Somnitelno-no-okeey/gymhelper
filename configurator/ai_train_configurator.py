import requests
import json

def generate_train_config(day_week,
                         muscle_groups,
                         difficulty,
                         train_place,
                         train_program,
                         train_type):
    prompt = {
        "modelUri": "gpt://b1gdb6f1n3b0uhbktan6/yandexgpt/rc",
        "completionOptions": {
            "stream": False,
            "temperature": 0.0,
            "maxTokens": "5000"
        },
        "messages": [
            {
                "role": "system",
                "text": "ТЫ тренер, твоя задача - это составление программ тренировок на неделю. "
                        "Тренировки бывают двух видов.Система с говорящим названием «фулбоди» подразумевает выполнение тренировки на все группы мышц за одно занятие. "
                        "Пару упражнений на ноги и ягодицы, еще несколько, чтобы прокачать спину и руки, и «на десерт» — пресс. Сплит-тренировка основана на разделении мышц по группам. "
                        "На каждую группу мышц отведен свой день. (Если тренировка, помечена как сплит, обозначай, за что отвечает каждый день) "
                        "Тренировки могут проходить как в зале, со спортивным оборудование, так и дома, без спортинветаря. "
                        "Упражнения делятся на три вида, простые, средние и сложные, а также подразделяются по группам мышц. "
                        "Тренировка должна включать 4-5 упражнений.Не нужно подробно описывать упражнение, лишь название, мышцы и количество повторений-подходов."
            },
            {
                "role": "user",
                "text": f"Составь программу на неделю. "
                        f"Тренировка: {train_program} "
                        f"Дни тренировок: {', '.join(day_week)} "
                        f"Уровень: {difficulty} "
                        f"Условия: {train_place} "
                        f"Тип тренировки: {train_type}"
                        f"Группы мышц: {', '.join(muscle_groups)} "
                        f"Отправь массив объектов, в каждом объекте будут поля: день недели, группа мышц, упражнения. Упражнения - массив минимум 3-5 объектов, в каждом объекте есть поля: название, повторения-подходы, например 2x30, без каких либо слов."
            }
        ]
    }


    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key AQVN3PeToob5d4c67OHkBKBJ_BUuKh2zJervWuEa"
    }
    
    output = requests.post(url, headers=headers, json=prompt).text
    json_output = json.loads(output)
    workout_plan = json.loads(json_output["result"]["alternatives"][0]["message"]["text"].strip("```"))
    return workout_plan
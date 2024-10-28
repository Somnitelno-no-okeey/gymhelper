import requests

def generate_workout_plan(days,
                         target_muscles,
                         difficulty,
                         conditions,
                         workout_type):
    prompt = {
        "modelUri": "gpt://b1gdb6f1n3b0uhbktan6/yandexgpt/rc",
        "completionOptions": {
            "stream": False,
            "temperature": 0.1,
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
                        f"Тренировка: {workout_type} "
                        f"Дни тренировок: {', '.join(days)} "
                        f"Уровень: {difficulty} "
                        f"Условия: {conditions} "
                        f"Группы мышц: {', '.join(target_muscles)} "
                        f"Отправь в виде json файла"
            }
        ]
    }


    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key AQVN3PeToob5d4c67OHkBKBJ_BUuKh2zJervWuEa"
    }
    output = requests.post(url, headers=headers, json=prompt).text
    with open("output.txt", "w", encoding="utf-8") as file:
        file.write(output)
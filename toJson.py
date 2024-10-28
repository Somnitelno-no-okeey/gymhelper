import json

def toJson(output_string):
    with open('output.txt', 'r', encoding='utf-8') as file:
        json_string = file.read()

    json_output = json.loads(json_string)
    workout_plan = json.loads(json_output["result"]["alternatives"][0]["message"]["text"].strip("```"))

    return workout_plan
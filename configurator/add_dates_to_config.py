import json
from datetime import date, datetime, timedelta

def add_dates_to_config(train_config, start_date_str):
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    week_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    
    week_days_ru = {
        "monday": "Понедельник",
        "tuesday": "Вторник",
        "wednesday": "Среда",
        "thursday": "Четверг",
        "friday": "Пятница",
        "saturday": "Суббота",
        "sunday": "Воскресенье"
    }
    
    months_ru = {
        "January": "Январь",
        "February": "Февраль",
        "March": "Март",
        "April": "Апрель",
        "May": "Май",
        "June": "Июнь",
        "July": "Июль",
        "August": "Август",
        "September": "Сентябрь",
        "October": "Октябрь",
        "November": "Ноябрь",
        "December": "Декабрь"
    }
    
    new_train_config = []
    for item in train_config:
        day_of_week = item["день недели"].lower()
        days_to_add = (week_days.index(day_of_week) - start_date.weekday() + 7) % 7
        current_date = start_date + timedelta(days=days_to_add)
        
        training_day = {
            "month": months_ru[current_date.strftime("%B")],
            "day": current_date.day,
            "dayWeek": week_days_ru[day_of_week],
            "exercises": []
        }
        
        for exercise in item["упражнения"]:
            training_day["exercises"].append({
                "name": exercise["название"],
                "repeat": exercise["повторения-подходы"]
            })
        
        new_train_config.append(training_day)

        next_week_date = current_date + timedelta(days=7)
        next_week_day = {
            "month": months_ru[next_week_date.strftime("%B")],
            "day": next_week_date.day,
            "dayWeek": week_days_ru[day_of_week],
            "exercises": training_day["exercises"].copy()
        }
        new_train_config.append(next_week_day)
    
    return new_train_config
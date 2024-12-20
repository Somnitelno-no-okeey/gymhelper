from datetime import date
from django.shortcuts import redirect, render
from configurator.ai_train_configurator import generate_train_config
from configurator.add_dates_to_config import add_dates_to_config
from configurator.models import TrainConfig

def configurator(request):
    if request.method == 'POST':
        config = TrainConfig()
        config.user = request.user
        config.train_place = request.POST.get('train-place')
        config.train_type = request.POST.get('train-type')
        config.train_program = request.POST.get('train-program')
        config.day_week = request.POST.getlist('day-week')
        config.muscle_groups = request.POST.getlist('muscle-groups')
        config.difficulty = request.POST.get('difficulty')
        current_date = str(date.today())
        config.train_config =  add_dates_to_config(generate_train_config(train_place=config.train_place,
                                                train_type=config.train_type,
                                                train_program=config.train_program,
                                                day_week=config.day_week,
                                                muscle_groups=config.muscle_groups,
                                                difficulty=config.difficulty), current_date)

        config.save()
        return redirect('calendar')

    return render(request, 'configurator/configurator.html')

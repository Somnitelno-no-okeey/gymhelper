import json
from django.shortcuts import render
from configurator.models import TrainConfig

def calendar(request):
    train_config = TrainConfig.objects.filter(user=request.user).first()
    completed_days = []
    event_date = []
    if request.method == 'POST':
        data = json.loads(request.body)
        completed_days_to_update = data.get('completedDays', [])
        if train_config:
            train_config.completedDays = completed_days_to_update
            train_config.save()
    if train_config:
        if train_config.completedDays is not None:
            completed_days = json.dumps(train_config.completedDays)
        else:
            completed_days = json.dumps([]) 
        if train_config.train_config is not None:
            event_date = json.dumps(train_config.train_config)
        else:
            event_date = json.dumps([]) 
    context = {
        'completed_days': completed_days,
        'event_date': event_date,
    }
    return render(request, 'train_calendar/calendar.html', context)
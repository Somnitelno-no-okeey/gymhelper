const daysTag = document.querySelector(".days");
const currentDate = document.querySelector(".current-month");
const prevNextIcon = document.querySelectorAll(".buttons-container button");
const daysWeekContainer = document.querySelector('.days-weeek');
const dayWeekTemplate = daysWeekContainer.querySelector('.day-week');

let date = new Date(),
currYear = date.getFullYear(),
currMonth = date.getMonth();

const daysWeek = {
    'Понедельник': 'пн',
    'Вторник': 'вт',
    'Среда': 'ср',
    'Четверг': 'чт',
    'Пятница': 'пт',
    'Суббота': 'сб',
    'Воскресенье': 'вс',
};

const months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль",
              "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"];

const renderCalendar = () => {
    let firstDayofMonth = (new Date(currYear, currMonth, 1).getDay() + 6) % 7,
    lastDateofMonth = new Date(currYear, currMonth + 1, 0).getDate(),
    lastDayofMonth = (new Date(currYear, currMonth, lastDateofMonth).getDay() + 6) % 7,
    lastDateofLastMonth = new Date(currYear, currMonth, 0).getDate();
    let liTag = "";

    for (let i = firstDayofMonth; i > 0; i--) {
        liTag += `<li class="inactive">${lastDateofLastMonth - i + 1}</li>`;
    }

    for (let i = 1; i <= lastDateofMonth; i++) {
        let isEventDay = eventDate.some(event => 
            event.month === months[currMonth] && event.day === i && currYear === new Date().getFullYear()
        ) ? "event" : "";
        let isToday = i === date.getDate() && currMonth === new Date().getMonth() 
                     && currYear === new Date().getFullYear() ? "current-day" : "";
        liTag += `<li class="${isToday} ${isEventDay}">${i}</li>`;
    }

    for (let i = lastDayofMonth; i < 6; i++) {
        liTag += `<li class="inactive">${i - lastDayofMonth + 1}</li>`
    }
    currentDate.innerText = `${months[currMonth]}`;
    daysTag.innerHTML = liTag;
}
renderCalendar();

prevNextIcon.forEach(icon => {
    icon.addEventListener("click", () => {
        currMonth = icon.classList.contains('prev') ? currMonth - 1 : currMonth + 1;

        if(currMonth < 0 || currMonth > 11) {
            date = new Date(currYear, currMonth, new Date().getDate());
            currYear = date.getFullYear();
            currMonth = date.getMonth();
        } else {
            date = new Date();
        }
        renderCalendar();
    });
});

const generateTrainingDayInfo = (dayData) => {
    const trainingDayInfo = document.querySelector('.training-day-info');
    const exercisesContainer = trainingDayInfo.querySelector('.exercises');
    trainingDayInfo.querySelector('.day-week').textContent = dayData.dayWeek;
    const exerciseContainerTemplate = exercisesContainer.querySelector('.exercise');
    exerciseContainerTemplate.style.display = 'flex';
    exercisesContainer.innerHTML = '';

    dayData.exercises.forEach((exercise) => {
        const exerciseContainer = exerciseContainerTemplate.cloneNode(true);
        exerciseContainer.querySelector('.exercise-name').textContent = exercise.name;
        exerciseContainer.querySelector('.exercise-repeat').textContent = exercise.repeat;
        exercisesContainer.append(exerciseContainer);
    });
};

const generateTodayTrainingInfo = () => {
    const matchedDayData = eventDate.find((event) => event.day == date.getDate() && event.month == months[currMonth] && currYear === new Date().getFullYear());
    if (matchedDayData) {
        generateTrainingDayInfo(matchedDayData);
    }
};

daysTag.addEventListener('click', (evt) => {
    const clickedDay = evt.target.textContent;
    const matchedEvent = eventDate.find((event) => event.day == clickedDay && event.month == months[currMonth] && currYear === new Date().getFullYear());

    if (matchedEvent) {
        daysTag.querySelectorAll('li').forEach((day) => {
            day.classList.remove('active');
        });
        evt.target.classList.add('active');

        generateTrainingDayInfo(matchedEvent);
    }
});

generateTodayTrainingInfo();

const generateCurrentWeekData = () => {
    const currentDate = new Date();
    const currentDay = currentDate.getDate();
    const currentDayWeek = (currentDate.getDay() + 6) % 7;

    const startCurrentWeek = new Date(currentDate);
    startCurrentWeek.setDate(currentDay - currentDayWeek);

    const endCurrentWeek = new Date(startCurrentWeek);
    endCurrentWeek.setDate(startCurrentWeek.getDate() + 6);

    let indexFirstTrainingDay = -1;
    let indexLastTrainingDay = -1;
    let attemptCount = 0;
    let maxAttempts = 7;

    while (indexFirstTrainingDay == -1 && attemptCount < maxAttempts) {
        const firstTrainingDay = eventDate.find((event) => event.day == startCurrentWeek.getDate() && event.month == months[startCurrentWeek.getMonth()]);
        if (firstTrainingDay) {
            indexFirstTrainingDay = eventDate.indexOf(firstTrainingDay);
        } else {
            startCurrentWeek.setDate(startCurrentWeek.getDate() + 1);
        }
        attemptCount++;
    }

    attemptCount = 0;

    while (indexLastTrainingDay == -1 && attemptCount < maxAttempts) {
        const lastTrainingDay = eventDate.find((event) => event.day == endCurrentWeek.getDate() && event.month == months[endCurrentWeek.getMonth()]);
        if (lastTrainingDay) {
            indexLastTrainingDay = eventDate.indexOf(lastTrainingDay);
        } else {
            endCurrentWeek.setDate(endCurrentWeek.getDate() - 1);
        }
        attemptCount++;
    }

    let currentWeekData;

    if (indexFirstTrainingDay != -1 && indexLastTrainingDay != -1) {
        currentWeekData = eventDate.slice(indexFirstTrainingDay, indexLastTrainingDay + 1);
    }

    return currentWeekData;
};

const filterData = () => {
    const currentWeekData = generateCurrentWeekData();
    if (!currentWeekData) {
        return currentWeekData;
    }
    const filteredData = currentWeekData.filter((dayData) =>
        !completedDays.some((completedDay) => completedDay.month === dayData.month && completedDay.day === dayData.day)
      );

    return filteredData;
};

const onFormSubmit = (daysData) => {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    const form = document.querySelector('.progress-form');
    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const selectedDays = Array.from(form.querySelectorAll('input[name="day-week"]:checked'));
        
        const markedDays = daysData.filter((dayData) => 
            selectedDays.some((selectedDay) => 
                dayData.dayWeek == selectedDay.value && 
                dayData.day == selectedDay.dataset.day && 
                dayData.month == selectedDay.dataset.month
            )
        );

        completedDays.push(...markedDays);

        daysData = daysData.filter(day => !markedDays.includes(day));
        renderProgressButtons(daysData);
        fillProgressBar();

        fetch('/calendar/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken,
            },
            body: JSON.stringify({
                completedDays: completedDays,
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                console.log('Данные успешно сохранены');
            }
        })
        .catch(error => {
            console.error('Ошибка отправки данных:', error);
        });
    });
};

const renderProgressButtons = (filteredData) => {
    daysWeekContainer.innerHTML = '';
    dayWeekTemplate.style.display = 'flex';

    filteredData.forEach((dayData) => {
        const dayWeekContainer = dayWeekTemplate.cloneNode(true);
        dayWeekContainer.querySelector('p').textContent = daysWeek[dayData.dayWeek];
        dayWeekContainer.querySelector('input').value = dayData.dayWeek;
        dayWeekContainer.querySelector('input').dataset.day = dayData.day;
        dayWeekContainer.querySelector('input').dataset.month = dayData.month;
        daysWeekContainer.append(dayWeekContainer);
    });
};

const fillProgressBar = () => {
    const bar = document.querySelector('.filled-bar');
    const progressCountContainer = document.querySelector('.progress-count');

    const lengthCurrentTrainingProgram = eventDate.length;
    const progresCount = Math.round((completedDays.length / lengthCurrentTrainingProgram) * 100);

    progressCountContainer.textContent = progresCount;
    bar.style.width = `${progresCount}%`;
};

const renderProgress = () => {
    const filteredData = filterData();

    if (filteredData) {
        renderProgressButtons(filteredData);
        onFormSubmit(filteredData);
    }

    fillProgressBar();
};

renderProgress();

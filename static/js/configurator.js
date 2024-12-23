let currentStep = 1;
let currentStepContainer = document.querySelector('.active-step');
let currentStepButton = document.querySelector('.step-btn.active');
let title = document.querySelector('.step-title');
const stepButtonContainer = document.querySelector('.step-button-container');
let stepButtons = stepButtonContainer.querySelectorAll('.step-btn');
const stepContainers = document.querySelectorAll('.step-container');
const nextStepButtons = document.querySelectorAll('.next-step');
const containersWithNextButton = document.querySelectorAll('.have-further-btn');
let titles = ['Где вы планируете тренироваться?','Какие тренировки вы предопчитаете?', 'Какой вид тренировок вы предпочитаете?', 'В какие дни вы планируете тренироваться?', 'Какие группы планируете тренировать?' , 'Выберите сложность программы'];
let availableStepContainers = [1, 2, 3, 4, 5, 6];

const delay = (ms) => {
    return new Promise(resolve => setTimeout(resolve, ms));
}

const initializeStepButtonListeners = () => {
    for (let stepButton of stepButtons) {
        stepButton.addEventListener('click', function() {
            if (stepButton.dataset.btn < currentStep) {
                currentStep = stepButton.dataset.btn;
                renderStep(currentStep);
            }
        });
    }
};

const updateButtonState = () => {
    for (let containerWithNextButton of containersWithNextButton) {
        const inputs = containerWithNextButton.querySelectorAll('input');
        const furtherButton = containerWithNextButton.querySelector('.next-step');
    
        if (furtherButton) {
            inputs.forEach(input => {
                input.addEventListener('change', () => {
                    const isSelected = Array.from(inputs).some(inp => inp.checked);
                    furtherButton.disabled = !isSelected;
                });
            });
        }
    }
};

const updateSubmitButton = () => {
    const submitButtonContainer = document.querySelector('.step-container[data-stage="6"]')
    const submitButton = submitButtonContainer.querySelector('.submit-btn');
    const inputs = submitButtonContainer.querySelectorAll('input');

    if (submitButton) {
        inputs.forEach(input => {
            input.addEventListener('change', () => {
                const isSelected = Array.from(inputs).some(inp => inp.checked);
                submitButton.disabled = !isSelected;
            });
        });
    }
};

const initializeNextStepButtonListeners = () => {
    for (let nextStepButton of nextStepButtons) {
        nextStepButton.addEventListener('click', function() {
            currentStep++;
            if (currentStep == 3) {
                const fork1 = document.querySelector('input[name="train-place"]:checked');
                const fork2 = document.querySelector('input[name="train-type"]:checked');
                if (fork2.value == 'cardio') {
                    availableStepContainers.splice(2,1);
                    availableStepContainers.splice(3,1);
                }
                else if (fork1.value == 'home') {
                    availableStepContainers.splice(2,1);
                }
                renderStepButtons();
            }
    
            if (currentStep >= 3 && !availableStepContainers.includes(currentStep)) {
                currentStep++;
            }
            renderStep(currentStep);
        });
    }
};

const renderStep = async (step) => {
    if (currentStepContainer.dataset.stage != step) {
        currentStepContainer.classList.add('hidden');
        title.classList.add('hidden');
        await delay(400);
        currentStepContainer.classList.remove('active-step');
        currentStepButton.classList.remove('active');

        for (let stepButton of stepButtons) {
            if (stepButton.dataset.btn == step) {
                stepButton.classList.add('active');
            }
        }

        for (let stepContainer of stepContainers) {
            if (stepContainer.dataset.stage == step) {
                stepContainer.classList.add('active-step');
                title.textContent = titles[step-1]
                await delay(50);
                title.classList.remove('hidden');
                stepContainer.classList.remove('hidden');
            }
        }

        currentStepContainer = document.querySelector('.active-step');
        currentStepButton = document.querySelector('.step-btn.active');
    }
};

const renderStepButtons = () => {
    stepButtonContainer.innerHTML = '';

    for (let i = 0; i < availableStepContainers.slice(2).length; i++) {
        const button = document.createElement('button');
        if (i == 0) {
            button.classList.add('active');
        }
        button.classList.add('step-btn');
        button.setAttribute('data-btn', availableStepContainers.slice(2)[i]);
        button.setAttribute('type', 'button');
        stepButtonContainer.appendChild(button);
    }

    stepButtons = stepButtonContainer.querySelectorAll('.step-btn');
    initializeStepButtonListeners();
};

initializeStepButtonListeners();
initializeNextStepButtonListeners();
updateButtonState();
updateSubmitButton();
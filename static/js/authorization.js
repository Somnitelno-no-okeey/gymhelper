const welcomeWrapper = document.querySelector('.welcome-wrapper');
const authorizationWrapper = document.querySelector('.authorization-wrapper');
const welcomeText = welcomeWrapper.querySelector('.text');
const button = document.querySelector('.authorization-button');
const forms = document.querySelectorAll('.authorization-container form');

const tl = gsap.timeline({ paused: true });

tl.to(welcomeWrapper, {duration: 1.4, ease: "power2.inOut", left: "50%"})
.to(welcomeWrapper, {duration: 0.7, ease: "power2.inOut", width: "57%", onComplete: switchContent}, "-=1.4")
.to(welcomeWrapper, {duration: 0.7, ease: "power2.inOut", width: "50%", onReverseComplete: switchContent}, "-=0.73")
.to(authorizationWrapper, {duration: 1.4, ease: "power2.inOut", left: "0%"}, "-=1.4")

const textStage = {
    'enter': 'Пожалуйста, войдите в систему, указав свои персональные данные',
    'register': 'Введите свои персональные данные и начните тренироваться с нами',
};

const buttonStage = {
    'enter': 'Войти',
    'register': 'Зарегистрироваться',
};

const changeContent = (element, dictionary) => {
    element.classList.add('hidden');
    setTimeout(() => {
        element.dataset.stage = element.dataset.stage == 'enter' ? 'register': 'enter';
        element.textContent = dictionary[element.dataset.stage];
        element.classList.remove('hidden')
    }, 250);
};

function switchContent() {
    changeContent(welcomeText, textStage);
    changeContent(button.querySelector('span'), buttonStage);
    forms.forEach((form) => {
        if (form.classList.contains('active')) {
            form.classList.remove('active');
            form.classList.add('hidden');
        } else {
            form.classList.add('active');
            form.classList.remove('hidden');
        }
    });
};


button.addEventListener('click', (evt) => {
    const buttonContent = evt.target.closest('.authorization-button');
    if (buttonContent && window.innerWidth >= 930) {
        if (buttonContent.querySelector('span').dataset.stage == 'enter') {
            tl.play();
        } else {
            tl.reverse();
        }
    } else {
        switchContent();
    }
});
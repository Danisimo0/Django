// Скрипт для desktop-приложения

// Получение ссылок на необходимые элементы DOM
var navLinks = document.querySelectorAll('nav ul li a');

// Обработчик события для навигационных ссылок
function handleNavLinkClick(event) {
    event.preventDefault();
    var targetSectionId = this.getAttribute('href').substring(1);
    var targetSection = document.getElementById(targetSectionId);

    // Прокручиваем страницу к целевому разделу
    window.scrollTo({
        top: targetSection.offsetTop,
        behavior: 'smooth'
    });
}

// Назначение обработчика события для каждой навигационной ссылки
for (var i = 0; i < navLinks.length; i++) {
    navLinks[i].addEventListener('click', handleNavLinkClick);
}

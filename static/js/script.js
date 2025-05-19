// static/js/script.js
document.addEventListener('DOMContentLoaded', () => {
    // Анимация чисел
    const animateCount = (element) => {
        const target = +element.dataset.target;
        const duration = 2000;
        const step = target / (duration / 10);
        let current = 0;

        const timer = setInterval(() => {
            current += step;
            element.textContent = Math.floor(current);
            if (current >= target) {
                clearInterval(timer);
                element.textContent = target;
            }
        }, 10);
    };

    // Наблюдатель для анимации
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const counters = entry.target.querySelectorAll('.count');
                counters.forEach(animateCount);
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    observer.observe(document.getElementById('stats'));

    // Параллакс эффект
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        document.querySelector('.hero-image').style.transform = 
            `translateY(${scrolled * 0.1}px)`;
    });

    // Анимация меню
    window.addEventListener('scroll', () => {
        const nav = document.querySelector('.nav');
        if (window.scrollY > 100) {
            nav.style.backgroundColor = 'rgba(255, 255, 255, 0.95)';
            nav.style.boxShadow = '0 2px 10px rgba(0,0,0,0.1)';
        } else {
            nav.style.backgroundColor = 'transparent';
            nav.style.boxShadow = 'none';
        }
    });
});


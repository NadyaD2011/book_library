// Простой JS для будущего расширения (например, лайки, модальные окна)
document.addEventListener('DOMContentLoaded', function () {
    console.log('MyMovies загружен!');

    // Пример: добавить эффект при наведении (уже есть в CSS, но можно расширить)
    const cards = document.querySelectorAll('.movie-card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.style.cursor = 'pointer';
        });
    });
});
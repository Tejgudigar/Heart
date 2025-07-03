function randomPosition(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

const stars = document.querySelectorAll('.sparkle.star');
const butterflies = document.querySelectorAll('.butterfly');

stars.forEach(star => {
    setInterval(() => {
        star.style.top = `${randomPosition(10, 90)}%`;
        star.style.left = `${randomPosition(10, 90)}%`;
    }, 3000); // Change position every 3 seconds
});

butterflies.forEach(butterfly => {
    setInterval(() => {
        butterfly.style.top = `${randomPosition(0, 100)}%`;
        butterfly.style.left = `${randomPosition(0, 100)}%`;
    }, 5000); // Change position every 5 seconds
});

let canvas = document.querySelector('.canvas');
let ctx = canvas.getContext('2d');

ctx.beginPath();
ctx.arc(ball.px, ball.py, ball.radius, 0, 2 * Math.PI, false);
ctx.fillStyle = 'green';
ctx.fill();

let ball = {
    radius: 4,
    px: Math.random() * width,
    py: Math.random() * height,
    vx: (2 * Math.random() - 1) * 10,
    vy: (2 * Math.random() - 1) * 10
};

function main_loop() {
    // update the ball's position
    // check if it hit a boundary
    // draw the ball
    window.requestAnimationFrame(main_loop);
}
window.requestAnimationFrame(main_loop);
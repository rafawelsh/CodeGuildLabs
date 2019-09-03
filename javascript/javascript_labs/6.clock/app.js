// part 1 done
var myVar = setInterval(clockwork, 1000);

function clockwork() {
    let today = new Date(); 

    document.getElementById('clock').innerHTML = today.toLocaleTimeString();
}

// part 2
const start = document.getElementById('start');
const stop = document.getElementById('stop');
const timerInterface = document.getElementById('timerInterface')

let timer = 0;
timerInterface.innerHTML = timer;

// let initial = new Date().setHours(0, 0, 0, 0);

start.addEventListener('click', function(){
        setInterval(function () {
        timerInterface.innerHTML = timer+=1;
    }, 1000);
});

// stop.addEventListener('click', function () {
//     clearInterval(function () {
//         timerInterface.innerHTML = timer += 1;
//     }, 1000);
// });

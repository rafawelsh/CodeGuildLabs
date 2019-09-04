// part 1 done
var myVar = setInterval(clockwork, 1000);

function clockwork() {
    let today = new Date(); 

    document.getElementById('clock').innerHTML = today.toLocaleTimeString();
}

// part 2
const start = document.getElementById('start');
const stop = document.getElementById('stop');
const pause = document.getElementById('pause');
const resume = document.getElementById('resume');
const timerInterface = document.getElementById('timerInterface')


var time = null;
var timeInterval = null;


start.addEventListener('click', function() {
    time = new Date();
    time.setHours(0, 0, 0, 0);
    timeInterval = setInterval(updateStopwatch, 1000);
    timerInterface.innerHTML = time;
});

stop.addEventListener('click', function() {
    clearInterval(timeInterval);
    timeInterval = null;
    time = new Date();
    time.setHours(0, 0, 0, 0);
    timerInterface.innerHTML = time
});

pause.addEventListener('click', function() {
    clearInterval(timeInterval);
    timeInterval = null
});

resume.addEventListener('click', function() {
    timeInterval = setInterval(updateStopwatch, 1000);
})

function updateStopwatch() {
    time.setSeconds(time.getSeconds() + 1);
    timerInterface.innerHTML = time;
};


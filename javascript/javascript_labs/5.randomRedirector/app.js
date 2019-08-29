var btn = document.getElementById('btn');
var start = document.getElementById('start');
var stop = document.getElementById('stop');
var frame = document.getElementById('theframe');

let urls = ['https://theuselessweb.com', 'https://rafaelcastellanoswelsh.com', 'http://corndog.io/','https://www.eyes-only.net/', 'https://thatsthefinger.com/'];


btn.addEventListener('click',function() {
    frame.src = urls[Math.floor(urls.length * Math.random())];
})






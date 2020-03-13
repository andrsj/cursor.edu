$(document).ready(function(){
    var check = $("input[type=checkbox]"), 
        arrcheck = [],
        radio = $("input[type=radio]"),
        arrradio = [],
        text  = $("#text"),
        answers = [[true,false,true,false],[false,true,false,false],'x + 1'];

    


    $(".check").click(function(){
        for(var i=0; i < check.length; i++){
            arrcheck[i] = check[i].checked;
        }
        for(var i=0; i < radio.length; i++){
            arrradio[i] = radio[i].checked;
        }

        var q = $("p.modaL");

        if( arrayIsarray(arrcheck,answers[0]) && arrayIsarray(arrradio,answers[1]) && text.val() == answers[2]){
            q.text("Всі задачі рішені правильно")
        }
        else{
            q.html("В тебе виникла помилка!<br>");

            if(arrayIsarray(arrcheck,answers[0]) != true){
                q.append("В першій задачі відповідь \"" + arrcheck + "\" вибрані не вірно!<br>");
            }
            if(arrayIsarray(arrradio,answers[1]) != true){
                q.append("В другій задачі відповідь \"" + arrradio + "\" вибрані не вірно!<br>");
            }
            if(text.val() != answers[2]){
                q.append("В третій задачі відповідь: \"" + text.val() + "\" введено не вірно<br>");
            }
        }
    });
})

function arrayIsarray(arr1,arr2){
    if(arr1.length != arr2.length) return false;
    for (let i=0; i<arr1.length; i++){
        if(arr1[i] != arr2[i]) return false;
    }
    return true;
}

var canvas, ctx;

var iStart = 0;
var bRightBut = false;
var bLeftBut = false;
var oBall, oPadd, oBricks;
var aSounds = [];
var iPoints = 0;
var iGameTimer;
var iElapsed = iMin = iSec = 0;
var sLastTime, sLastPoints;

//об"єкти
function Ball(x, y, dx, dy, r) {
    this.x = x;
    this.y = y;
    this.dx = dx;
    this.dy = dy;
    this.r = r;
}
function Padd(x, w, h, img) {
    this.x = x;
    this.w = w;
    this.h = h;
    this.img = img;
}
function Bricks(w, h, r, c, p) {
    this.w = w;
    this.h = h;
    this.r = r; // рядки
    this.c = c; // колонки
    this.p = p; // палка
    this.objs;
    this.colors = ['#9d9d9d', '#f80207', '#feff01', '#0072ff', '#fc01fc', '#03fe03']; // кольори для кубиків
}



function clear() { // очищення функції канвас
    ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);

    // задній фон
    ctx.fillStyle = '#111';
    ctx.fillRect(0, 0, ctx.canvas.width, ctx.canvas.height);
}

function drawScene() { // головна функція
    clear(); // очищення канвас

    // кулька
    ctx.fillStyle = '#f66';
    ctx.beginPath();
    ctx.arc(oBall.x, oBall.y, oBall.r, 0, Math.PI * 2, true);
    ctx.closePath();
    ctx.fill();

    if (bRightBut)
        oPadd.x += 5;
    else if (bLeftBut)
        oPadd.x -= 5;

    // палка
    ctx.drawImage(oPadd.img, oPadd.x, ctx.canvas.height - oPadd.h);

    // кубики
    for (i=0; i < oBricks.r; i++) {
        ctx.fillStyle = oBricks.colors[i];
        for (j=0; j < oBricks.c; j++) {
            if (oBricks.objs[i][j] == 1) {
                ctx.beginPath();
                ctx.rect((j * (oBricks.w + oBricks.p)) + oBricks.p, (i * (oBricks.h + oBricks.p)) + oBricks.p, oBricks.w, oBricks.h);
                ctx.closePath();
                ctx.fill();
            }
        }
    }

    
    iRowH = oBricks.h + oBricks.p;
    iRow = Math.floor(oBall.y / iRowH);
    iCol = Math.floor(oBall.x / (oBricks.w + oBricks.p));

    // збиття кубиків
    if (oBall.y < oBricks.r * iRowH && iRow >= 0 && iCol >= 0 && oBricks.objs[iRow][iCol] == 1) {
        oBricks.objs[iRow][iCol] = 0;
        oBall.dy = -oBall.dy;
        iPoints++;

        aSounds[0].play(); 
    }
    // позиція кульки по Х
    if (oBall.x + oBall.dx + oBall.r > ctx.canvas.width || oBall.x + oBall.dx - oBall.r < 0) {
        oBall.dx = -oBall.dx;
    }

    if (oBall.y + oBall.dy - oBall.r < 0) {
        oBall.dy = -oBall.dy;
    } else if (oBall.y + oBall.dy + oBall.r > ctx.canvas.height - oPadd.h) {
        if (oBall.x > oPadd.x && oBall.x < oPadd.x + oPadd.w) {
            oBall.dx = 10 * ((oBall.x-(oPadd.x+oPadd.w/2))/oPadd.w);
            oBall.dy = -oBall.dy;

            aSounds[2].play();
        }
        else if (oBall.y + oBall.dy + oBall.r > ctx.canvas.height) {
            clearInterval(iStart);
            clearInterval(iGameTimer);

            // HTML5 Local storage - save values
            localStorage.setItem('last-time', iMin + ':' + iSec);
            localStorage.setItem('last-points', iPoints);

            aSounds[1].play(); 
        }
    }

    oBall.x += oBall.dx;
    oBall.y += oBall.dy;

    ctx.font = '16px Verdana';
    ctx.fillStyle = '#fff';
    iMin = Math.floor(iElapsed / 60);
    iSec = iElapsed % 60;
    if (iMin < 10) iMin = "0" + iMin;
    if (iSec < 10) iSec = "0" + iSec;
    ctx.fillText('Time: ' + iMin + ':' + iSec, 600, 520);
    ctx.fillText('Points: ' + iPoints, 600, 550);

    if (sLastTime != null && sLastPoints != null) {
        ctx.fillText('Last Time: ' + sLastTime, 600, 460);
        ctx.fillText('Last Points: ' + sLastPoints, 600, 490);
    }
}


function init(){
    canvas = document.getElementById('scene');
    ctx = canvas.getContext('2d');

    var width = canvas.width;
    var height = canvas.height;

    var padImg = new Image();
    padImg.src = 'images/padd.png';
    padImg.onload = function() {};

    oBall = new Ball(width / 2, 550, 0.5, -5, 10); // початкова позиція кульки
    oPadd = new Padd(width / 2, 120, 20, padImg); // початкова позиція палки
    oBricks = new Bricks((width / 8) - 1, 20, 6, 8, 2); // початкова позиція кубиків

    oBricks.objs = new Array(oBricks.r); // fill-in bricks
    for (i=0; i < oBricks.r; i++) {
        oBricks.objs[i] = new Array(oBricks.c);
        for (j=0; j < oBricks.c; j++) {
            oBricks.objs[i][j] = 1;
        }
    }

    aSounds[0] = new Audio('media/snd1.wav');
    aSounds[0].volume = 0.9;
    aSounds[1] = new Audio('media/snd2.wav');
    aSounds[1].volume = 0.9;
    aSounds[2] = new Audio('media/snd3.wav');
    aSounds[2].volume = 0.9;

    drawScene();
    iGameTimer = setInterval(countTimer, 1000); // час

    // HTML5 Local storage - get values
    sLastTime = localStorage.getItem('last-time');
    sLastPoints = localStorage.getItem('last-points');

    $(window).keydown(function(event){ //керування клавішами
        switch (event.keyCode) { 
            case 37:
                bLeftBut = true;
                break;
            case 39: 
                bRightBut = true;
                break;
        }
    });
    $(window).keyup(function(event){ //
        switch (event.keyCode) {
            case 37: 
                bLeftBut = false;
                break;
            case 39:
                bRightBut = false;
                break;
        }
    });

    var iCanvX1 = $(canvas).offset().left;
    var iCanvX2 = iCanvX1 + width;
    $('#scene').mousemove(function(e) { // керування мишею
        if (e.pageX > iCanvX1 && e.pageX < iCanvX2) {
            oPadd.x = Math.max(e.pageX - iCanvX1 - (oPadd.w/2), 0);
            oPadd.x = Math.min(ctx.canvas.width - oPadd.w, oPadd.x);
        }
    });
};

function countTimer() {
    iElapsed++;
}

var restart = () => {
	clearInterval(iStart)
	clearInterval(iGameTimer)
	oBall = new Ball(canvas.width / 2, 550, 0.5, -5, 10);
    iStart = setInterval(drawScene, 10);

    ctx.font = '16px Verdana';
    ctx.fillStyle = '#fff';
    iMin = Math.floor(iElapsed / 60);
    iSec = iElapsed % 60;
    if (iMin < 10) iMin = "0" + iMin;
    if (iSec < 10) iSec = "0" + iSec;

    ctx.fillText('Time: ' + iMin + ':' + iSec, 600, 520);
    ctx.fillText('Points: ' + iPoints, 600, 550);

    if (sLastTime != null && sLastPoints != null) {
        ctx.fillText('Last Time: ' + sLastTime, 600, 460);
        ctx.fillText('Last Points: ' + sLastPoints, 600, 490);
    }
    
    ctx.fillText('Time: ' + iMin + ':' + iSec, 600, 520);
    ctx.fillText('Points: ' + iPoints, 600, 550);
}
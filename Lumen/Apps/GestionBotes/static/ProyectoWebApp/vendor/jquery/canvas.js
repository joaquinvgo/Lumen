const lensRadius = 220;  
const grabPointOffsetX = 175;  
const grabPointOffsetY = 175;  
var zoom;  
   
var canvas, context;  
var mouseX, mouseXConstrained, mouseY, mouseYConstrained;  
var xSource, ySource;  
   
var xMinium, xMaximum, yMinium, yMaximum; 




function init() {  
  
    canvas = document.getElementById("canvas");  
    canvas.addEventListener("mousemove", mouseTrack, false);  
    canvas.addEventListener("touchmove", touchTrack, true);  
  
    context = canvas.getContext("2d");  
  
    xMinium = canvas.offsetLeft + 198 - grabPointOffsetX;  
    xMaximum = canvas.offsetLeft + 570 - grabPointOffsetX;  
    xMinium = canvas.offsetLeft + 198 - grabPointOffsetY;  
    xMaximum = canvas.offsetLeft + 800 - grabPointOffsetY;  
  
    mouseX = 220 + canvas.offsetLest;  
    mouseY = 720 + canvas.offsetTop;  
  
    zoom - document.getElementById("lagreImage").width / canvas.width * 0.8;  
    drawMagGlass();  
  
}
// function declaration
function drawMagGlass() {  
  
    constrainPosition();  
    xSource = 2 * mouseXConstrained - zoom * lensRadius + 2 * grabPointOffsetX;  
    ySource = 2 * mouseYConstrained - zoom * lensRadius + 2 * grabPointOffsetY;  
  
    context.clearRect(0, 0 canvas.width, canvas.height);  
    context.save();  
  
    context.beginPath();  
    context.arc(mouseXConstrained + grabPointOffsetX, mouseYConstrained - grabPointerOffsetY, lensRadius, 0, 2 * Math.PI, false);  
    context.closePath();  
    context.clip();  
}  
  
// Now filling in the gaps remained in  
function constrainPosition() {  
  
    if (mouseX < xMinium) {  
        mouseXConstrained = xMinium - canvas.offsetLeft;  
    } else if (mouseX > xMaximum) {  
        mouseXConstrained = xMaximum - canvas.offsetLeft;  
    } else {  
        mouseXConstrained = mouseX - canvas.offsetLeft;  
    }  
  
    if (mouseY < yMinium) {  
        mouseYConstrained = yMinium - canvas.offsetLeft;  
    } else if (mouseX > xMaximum) {  
        mouseYConstrained = yMaximum - canvas.offsetLeft;  
    } else {  
        mouseYConstrained = mouseY - canvas.offsetLeft;  
    }  
  
}  
  
// finally calling of mousetrack function  
function mouseTrack(e) {  
&Magnify Effectnbsp; 
    if (!e) {  
        var e = event;  
    }  
    mouseX = e.clientX +  
        ((document.documentElement.scrollLeft) ?  
            document.documentElement.scrollLeft : document.body.scrollLeft);  
    mouseY = e.clientY +  
        ((document.documentElement.scrollTop) ?  
            document.documentElement.scrollTop : document.body.scrollTop);  
  
    drawMagGlass();  
  
}  
  
function touchTrack(e) {  
  
    if (!e) {  
        var e = event;  
    }  
  
    mouseX = e.targetTouches[e].pageX;  
    mouseY = e.targetTouches[e].pageY;  
  
} 
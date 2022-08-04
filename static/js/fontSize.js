let body = document.getElementsByTagName("body")[0];

let pTags = document.getElementsByTagName('p');
let decreaseSign = document.getElementById('decrease');
let increaseSign = document.getElementById('increase');


decreaseSign.onclick = function () {
    body.style.fontSize = "10px"
    return false
};

increaseSign.onclick = function () {
    body.style.fontSize = "50px"
    return false
};





console.log("dupa2")
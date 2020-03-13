function show(){
    var text = document.getElementsByTagName("input")[0];
    var checkboxes = document.getElementsByClassName('checkbox');
    var val = parseFloat(text.value);
    if (checkboxes[0].checked == true) {
        alert(val * val)
    }
    if (checkboxes[1].checked == true) {
        alert(val * val * Math.PI )
    }
    if (checkboxes[2].checked == true) {
        alert(val * val / 2)
    }
}

var k = []

function answer(a,b){
    let e = document.getElementsByTagName("form")[a].children[b].children[0].checked
    if(e == true) {
        alert("+")
        if(k[a-1] == undefined) k.push(true)
    }
    else{
        alert("-")
        if(k[a-1] == undefined) k.push(false)
    }
    console.log(k)
}

function counter() {
    let count = 0;
    document.getElementById("answer").innerHTML = "Правильні відповідді: "
    for (let i = 0; i < k.length; i++){
        if(k[i] == true) {
            count++;
            document.getElementById("answer").innerHTML +=  (i+1) + " ";
        }
    }
    document.getElementById("answer").innerHTML += "<br>К-сть правильних відповідей: " + count ;
    document.getElementById("again").style.display = "inline-block"
}

function empty(){
    let e = document.getElementsByTagName("form")
    for (let i = 1; i < e.length - 1; i++){
        if (e[i].children[0].children[0].checked == false && e[i].children[2].children[0].checked == false && e[i].children[4].children[0].checked == false){
            document.getElementById("noanswer").innerHTML += "Не стоїть відповідь біля питання " + i + "<br>";
        }
    }

}

function clr(){
    for (let i = 0; i < k.length; i++){
        k.pop();
    }

    let e = document.getElementsByTagName("input")
    for (let i = 0; i < e.length; i++){
        e[i].checked = false;
    }

    document.getElementById("again").style.display = "none"
    document.getElementById("noanswer").innerHTML = ""
    document.getElementById("answer").innerHTML = ""
}





function select(a){
    console.table(a,a.nextElementSibling);
    console.log(a.options);
    let newOption = new Option('0','0');
    switch(a.selectedIndex){
        case 0:
            while (a.nextElementSibling.firstChild) {
                a.nextElementSibling.removeChild(a.nextElementSibling.firstChild);
            }
            massiveChars = genCharArray("a","g");
            for(let i = 0; i < massiveChars.length; i++){
                newOption = new Option(massiveChars[i], massiveChars[i]);
                a.nextElementSibling.append(newOption);
            }
            break;
        case 1:
            while (a.nextElementSibling.firstChild) {
                a.nextElementSibling.removeChild(a.nextElementSibling.firstChild);
            }
            massiveChars = genCharArray("h","n");
            for(let i = 0; i < massiveChars.length; i++){
                newOption = new Option(massiveChars[i], massiveChars[i]);
                a.nextElementSibling.append(newOption);
            }
            break;
        case 2:
            while (a.nextElementSibling.firstChild) {
                a.nextElementSibling.removeChild(a.nextElementSibling.firstChild);
            }
            massiveChars = genCharArray("o","u");
            for(let i = 0; i < massiveChars.length; i++){
                newOption = new Option(massiveChars[i], massiveChars[i]);
                a.nextElementSibling.append(newOption);
            }
            break;
        case 3:
            while (a.nextElementSibling.firstChild) {
                a.nextElementSibling.removeChild(a.nextElementSibling.firstChild);
            }
            massiveChars = genCharArray("v","z");
            for(let i = 0; i < massiveChars.length; i++){
                newOption = new Option(massiveChars[i], massiveChars[i]);
                a.nextElementSibling.append(newOption);
            }
            break;
    }
}

function genCharArray(charA, charZ) {
    var a = [], // massive
        i = charA.charCodeAt(0), //first element 
        j = charZ.charCodeAt(0); //last element
    for (; i <= j; ++i) {
        a.push(String.fromCharCode(i));
    }
    return a; //return massive
}
// genCharArray('a', 'z'); // ["a", ..., "z"]
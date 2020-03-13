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
    if (checkboxes[3].checked == true) {
        alert(2 * Math.PI * val)
    }
    if (checkboxes[4].checked == true) {
        alert(Math.PI * val * val * val * 4 / 3)
    }
    // console.log(checkboxes)
    // alert(checkboxes[0].checked)
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

    // console.log(document.getElementsByTagName("input"))
    alert("Пройдіть тест!")
    let e = document.getElementsByTagName("input")
    for (let i = 0; i < e.length; i++){
        e[i].checked = false;
    }
    // document.getElementsByTagName("input").checked = false
    // console.log(k)

    document.getElementById("again").style.display = "none"
    document.getElementById("noanswer").innerHTML = ""
    document.getElementById("answer").innerHTML = ""
}

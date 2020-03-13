var k = []

function answer(a,b){
    let e = document.getElementsByTagName("form")[a-1].children[b].children[0].checked
    if(e == true) {
        alert("+")
        if(k[a] == undefined) k.push(true)
    }
    else{
        alert("-")
        if(k[a] == undefined) k.push(false)
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
    console.log(e)
    for (let i = 0; i < e.length; i++){
        if (e[i].children[0].children[0].checked == false && e[i].children[2].children[0].checked == false && e[i].children[4].children[0].checked == false){
            document.getElementById("noanswer").innerHTML += "Не стоїть відповідь біля питання " + (i + 1) + "<br>";
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

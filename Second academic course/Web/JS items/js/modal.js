var modal = document.getElementById("myVanilaModal");
var button = document.getElementById("myVanilaModalbtn");
var span = document.getElementsByClassName("closed")[0];

button.onclick = function(){
    modal.style.display = "block";
}
span.onclick = function(){
    modal.style.display = "none";
}
window.onclick = function(event){
    if(event.target == modal){
        modal.style.display = "none";
    }
}
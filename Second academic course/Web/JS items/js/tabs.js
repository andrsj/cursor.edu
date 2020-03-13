var tab;
var tabContent;

window.onload = function(){
    tabContent = document.getElementsByClassName("tabs_content");
    tab = document.getElementsByClassName("tab");
    hideTabsContent(1);
}

function hideTabsContent (n){
    for( var i = n; i < tabContent.length; i++){
        tabContent[i].classList.remove("show");
        tabContent[i].classList.add("hide");
        tab[i].classList.remove("whiteborder");
    }
}

document.getElementById("tabs").onclick = function(event){
    var target = event.target;
    if (target.className == "tab"){
        for (var i = 0; i < tab.length; i++){
            if(target == tab[i]){
                showTabsContent(i);
                break;
            }
        }
    }
}

function showTabsContent(a){
    if (tabContent[a].classList.contains("hide")){
        hideTabsContent(0);
        tab[a].classList.add("whiteborder");
        tabContent[a].classList.remove("hide");
        tabContent[a].classList.add("show");
    }
}
var ID = false;
var elem = false;

function displaylist(a,event){
    if(elem != false){
        hidelist(elem);
        elem = false;
    }
    a.children[1].style.display = 'block';
    if (event.type == "mouseover"){
        ID = event.target.id;
        elem = event.target;
    }
    console.table(elem,ID,"Show1");
    if (event.type == "click") {
        ID = event.target.id;
        if( elem != false) {
            hidelist(elem);
            elem = a;
        } else {
        elem = a;
        }
    }
    console.table(elem,ID,"Show2");
}
function hidelist(a){
    a.children[1].style.display = 'none';
    console.table(elem,ID,"Hide");
    elem = false;
}
function check(event){
    if(event.target.id != ID){
        if(event.target.children.length == 0){
            // console.log();
        } else
        hidelist(elem);
    }
    console.table(elem,ID,"check");
}

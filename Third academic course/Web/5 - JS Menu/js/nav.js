let nav = document.getElementsByTagName("nav")[0]

for (i of nav.children){
    let child = i
    child.onmouseover = () => {display(child)}
    child.onmouseleave = () =>{hide(child)}
    for(j of child.children){
        if(j.tagName != "P"){
            let child2 = j
            for(k of child2.children){
                let child3 = k
                child3.onmouseover = () => {display(child3)}
                child3.onmouseleave = () => {hide(child3)}
                // for(l of child3.firstElementChild.children){
                //     let child4 = l
                    // child4.onmouseover = () =>{console.log(child4,child4.innerText)}
                // }
            }
        }
    }
}

const display = (elem) =>{
    for(i of elem.children){
        if(i.tagName != "P"){
            let block = i
            block.style.display = "block"
        }
    }
}

const hide = (elem) =>{
    for(i of elem.children){
        if(i.tagName != "P"){
            let block = i
            block.style.display = "none"
        }
    }
}


// nav
// menu        menu        menu
// p   sub     p   sub     p   sub

//     div
//     div
//     div

//     suub

//     div
//     div
//     div

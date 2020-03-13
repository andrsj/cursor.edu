let nav = document.getElementsByTagName("nav")[0]
let menuItems = [
    ["Розділи","Корисні посилання","Аккаунт"],
    [
        ["Розділ 1a","Розділ 2a","Розділ 3a"],//,"Розділ 4а"],
        ["Розділ 1b","Розділ 2b","Розділ 3b"],
        ["Розділ 1c","Розділ 2c","Розділ 3c"]
    ],
    [ // Масив посилань
        [ // Масив посилань для першого меню
        // [["Home","../index.html"],["Select","../index/select.html"],["Calculator","../index/calculator.html"]],
            [["Quest","../quest.html"],["Select","../index/select.html"],["Calculator","../index/calculator.html"]],
            [["Home","../index.html"]],
            [[131,"#"]],
            // [[141,"#"],[142,"#"]]
        ],
        [ // Масив посилань для другого меню
            [[211,"#"]],
            [[221,"#"],[222,"#"],[223,"#"]],
            [[231,"#"]],
            // false
        ],
        [ // Масив посилань для третього меню
            [[311,"#"]],
            [[321,"#"]],
            [[331,"#"],[332,"#"],[333,"#"]],
            // false
        ]
    ]
]


for(let i = 0; i < menuItems[0].length; i++){
    let menu = document.createElement("div")
    menu.className = "menu"
    menu.innerHTML = `<p>${menuItems[0][i]}</p><div class="sub"></div>`
    // menu - i тий елемент
    // menu children[1] - Блок для 1го підменю
    for (let j = 0; j < menuItems[1][0].length; j++){
        // console.log(i,j)
        menu.children[1].innerHTML += `<div>${menuItems[1][i][j]}</div>`
        // menu children[1].children[j] - Вміст блоку 1го підменю
        // menu children[1].children[j].children[0] - Блок для 2го підменю
        if (menu.children[1].children[j].children.length == 0)
            if (i != menuItems[0].length - 1)
                menu.children[1].children[j].innerHTML += `<div class='suub'></div>`
            else
                menu.children[1].children[j].innerHTML += `<div class='suubr'></div>`
        // console.log(menu.children[1].children[j].children[0])
        for (let k = 0; k < menuItems[2][i][j].length; k++){
            // if (menuItems[2][i][j][k])
            // console.log(menuItems[2][i][j],i,j,k)
            menu.children[1].children[j].children[0].innerHTML += `<div><a href='${menuItems[2][i][j][k][1]}'>${menuItems[2][i][j][k][0]}</a></div>`
        }
    }
    nav.appendChild(menu)
}

let clean = document.createElement("div")
clean.style.height = nav.style.height
clean.style.marginBottom = "100px"
nav.nextElementSibling.appendChild(clean)



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
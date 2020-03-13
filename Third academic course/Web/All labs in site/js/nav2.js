let nav = document.getElementsByTagName("nav")[0]
let menuItems = [
    ["Головне","Лабораторні","Інше"],
    [
        ["Розділ 1a","4 лабораторна","Розділ 3a"],//,"Розділ 4а"],
        ["Розділ 1b","Форми та тест jQuery","Розділ 3b"],
        ["Розділ 1c","Розділ 2c","Пусті посилання"]
    ],
    [ // Масив посилань
        [ // Масив посилань для першого меню
            [["Home","../index.html"]],
            [["Quest","../index/quest.html"],["Calendar","../index/calendar.html"],["Calculator","../index/calculator.html"]],
            [["Select","../index/select.html"]],
            // [[141,"#"],[142,"#"]]
        ],
        [ // Масив посилань для другого меню
            [["Carousel","../index/carousel-multy.html"]],
            [["Form","../index/form.html"],["Form 2","../index/form7.html"],["Test jQuery","../index/jquery.html"]],
            [["Пусто","#"]],
            // false
        ],
        [ // Масив посилань для третього меню
            [["Google","https://www.google.com/"]],
            [["Wikipedia","https://uk.wikipedia.org/wiki/%D0%92%D1%96%D0%BA%D1%96"]],
            [[1,"#"],[2,"#"],[3,"#"]],
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
            // console.log(menuItems[2][i][j],menuItems[2][i][j][k])
            // console.log(menu.children[1].children[j])
            if(menuItems[2][i][j].length == 1){
                menu.children[1].children[j].innerHTML = `<a href='${menuItems[2][i][j][k][1]}'>${menuItems[2][i][j][k][0]}</a>`
            }
            // console.log(menu.children[1].children[j].children[0])
            if (menu.children[1].children[j].children[0] !== undefined && menu.children[1].children[j].children[0].tagName != "A")
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
        if(i.tagName != "P" && i.tagName != "A"){
            let block = i
            block.style.display = "block"
        }
    }
}

const hide = (elem) =>{
    for(i of elem.children){
        if(i.tagName != "P" && i.tagName != "A"){
            let block = i
            block.style.display = "none"
        }
    }
}
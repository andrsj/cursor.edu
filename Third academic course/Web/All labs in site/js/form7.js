const checkname = firstname =>{

    let filter = [
        /^$/,
        /'[a-z]*'/,
        /^\s*[a-z]/,
        /\s[a-z]-/,
        /[A-Z]-/,
        /[^A-Za-z\s-']/,
        /\s[a-zA-Z]\s/,
        /\s[a-zA-Z]$/,
        /^[a-zA-Z]$/,
        /[A-Z][a-z]*[A-Z]/,
        /[a-z]+[A-Z]/,
        /''/,
        /'\s/,
        /\s'/,
        /'$/,
        /--/,
        /'-/,
        /-[a-zA-Z]\s*$/,
        /-\s{2,}/,
        /-'/,
        /-$/,
        /-\s$/,
        /^\s+$/
    ]

    // console.clear()
    for (i of filter){
        // console.log(i,i.test(firstname.value))
        if ( i.test(firstname.value)) {
            // ERROR
            firstname.style.border = "1px black solid"
            firstname.style.borderBottom = "2px red solid"
            return false
            break
        }
        else{
            // TRUE
            firstname.style.border = "1px black solid"
            firstname.style.borderBottom = "2px green solid"
        }
    }
    return true
}

const checklastname = lastname => {

    let filter = [
        /^$/,
        /'[a-z]*'/,
        /^\s*[a-z]/,
        /\s[a-z]-/,
        /[A-Z]-/,
        /[^A-Za-z\s-']/,
        /\s[a-zA-Z]\s/,
        /\s[a-zA-Z]$/,
        /^[a-zA-Z]$/,
        /[A-Z][a-z]*[A-Z]/,
        /[a-z]+[A-Z]/,
        /''/,
        /'\s/,
        /\s'/,
        /'$/,
        /--/,
        /'-/,
        /-[a-zA-Z]\s*$/,
        /-\s{2,}/,
        /-'/,
        /-$/,
        /-\s$/,
        /^\s+$/
    ]

    // console.clear()
    for (i of filter){
        // console.log(i,i.test(lastname.value))
        if ( i.test(lastname.value)) {
            // ERROR
            lastname.style.border = "1px black solid"
            lastname.style.borderBottom = "2px red solid"
            return false
            break
        }
        else{
            // TRUE
            lastname.style.border = "1px black solid"
            lastname.style.borderBottom = "2px green solid"
        }
    }
    return true
}

const checkdate = date => {
    let filter = /^((0[1-9])|([12]\d)|(3[01]))[\./-]((0[1-9])|(1[012]))[\./-]((19[2-9]\d)|(20[01]\d)|(\d\d))$/
    if ( !filter.test(date.value) ) {
        date.style.border = "1px black solid"
        date.style.borderBottom = "2px red solid"
        return false
    }
    else {
        date.style.border = "1px black solid"
        date.style.borderBottom = "2px green solid"
    }
    return true
}

const checkemail = email => {
    let filter = [
        /^$/,
        /^@$/,
        /[^a-z\d-_@\.\s]/,
        /\.\./,
        /[0-9a-z-_@\.]\s+[0-9a-z-_@\.]/,
        /\s\.\s/,
        /\.@\./,
        /\.@/,
        /@\./,
        /-@-/,
        /@-/,
        /-@/,
        /[^0-9a-z_]@[^0-9a-z_]/,
        /@@/,
        /^[^@]$/,
        /\s\d/,
        /^\d/,
        /^\s*[^a-z]/,
        /--/,
        /-\./,
        /\.-/,
        /-$/,
        /-\s/,
        /\.$/,
        /^\s*\.[a-z]/,
        /@[^a-z]/,
        /@.*\.\d/,
        /@([a-z]+\.[a-z]+){8,}/,
        /@\s/,
        /@[a-z]+(\s|$)/,
        /@$/,
        // /^.*@{0}.*$/,
        /[a-z]{5,}\s*$/,
        /\.[a-z]{0,1}\s*$/,
        /\.([^a-z])+\s*$/
    ]

    // console.clear()
    for (i of filter){
        // console.log(i,i.test(email.value))
        if ( i.test(email.value)) {
            // ERROR
            email.style.border = "1px black solid"
            email.style.borderBottom = "2px red solid"
            return false
            break
        }
        else{
            // TRUE
            email.style.border = "1px black solid"
            email.style.borderBottom = "2px green solid"
        }
    }
    return true
}

const checklanguage = (arr) => {
    let iter = 0;
    for(i of arr){
        if(i.checked) iter += 1;
    }
    if(iter == 0){
        alert("Ви не вибрали ніоднієї мови!")
        document.querySelector(".language").style.color = "red"
        return false
    } else
        document.querySelector(".language").style.color = "black"
    return true
}

const checktext = text => {
    if(text.value.length > 500){
        alert("Багато тексту! Більше 500 символів")
        text.style.borderBottom = "2px solid red"
        return false
    } else {
        text.style.borderBottom = "2px solid green"
        return true
    }
}

const checkphoto = photo =>{
    if(!/(\.jpg|\.png)$/.test(photo.value)){
        alert("Ви вибрали не фотографію")
        return false
    }
    return true
}

const checkpass = (password, a = false) => {
    // let filter = /((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#])){6,15}/
    let filter = /((?=.*\d)(?=.*[a-z])(?=.*[A-Z])){6,15}/
    if ( !filter.test(password.value) ) {
        password.style.border = "1px black solid"
        password.style.borderBottom = "2px red solid"
        return false
    } else {
        password.style.border = "1px black solid"
        password.style.borderBottom = "2px green solid"
        
    }
    if(a){
        if (password.value != document.getElementById("pass2").value){
            document.getElementById("pass2").style.border = "1px black solid"
            document.getElementById("pass2").style.borderBottom = "2px red solid"
            return false
        } else {
            document.getElementById("pass2").style.border = "1px solid black"
            document.getElementById("pass2").style.borderBottom = "2px solid green"
        }
    }
    return true
}
let valid = false,
    firstname = document.getElementById("firstname"),
    lastname = document.getElementById("lastname"),
    date = document.getElementById("date"),
    email = document.getElementById("email"),
    textarea = document.getElementsByTagName("textarea")[0],
    photo = document.querySelector("input[type='file']"),
    password = document.getElementById("pass1"),
    languages = document.querySelectorAll("input[type='checkbox']");

const validate = () => {


    console.clear()
    console.log(valid,0)
    valid = checkname(firstname)
    if(!valid) return valid
    console.log(valid,1)
    if(!valid) return valid

    valid = checklastname(lastname)
    console.log(valid,2)
    if(!valid) return valid

    valid = checkdate(date)
    console.log(valid,3)
    if(!valid) return valid

    valid = checkemail(email)
    console.log(valid,4)
    if(!valid) return valid

    valid = checktext(textarea)
    console.log(valid,5)
    if(!valid) return valid

    valid = checkphoto(photo)
    console.log(valid,6)
    if(!valid) return valid

    valid = checklanguage(languages)
    console.log(valid,7)
    if(!valid) return valid

    valid = checkpass(password,true)
    console.log(valid,8)
    if(!valid) return valid
    else return valid
}




const printinfo = valid =>{
    let div = document.querySelector("div.form"),
        arr = [firstname,lastname,date,email,textarea,photo,password,languages],
        text = ["Ім'я","Прізвище","Дату народження","Електронну адресу","Опис","Пароль"]

    if (valid){
        div.innerHTML = "<p>Ви ввели:</p> <br>"
        let j = 0
        for(i of arr){
            if (i.type != "file" && i.tagName != undefined){
                div.innerHTML += `<p>${text[j]} : ${i.value}</p> <br>`
                console.log(i)
                j++
            }
        }
        let img = document.createElement('img')
        img.src = URL.createObjectURL(photo.files[0])
        img.style.width = "100px"
        img.style.height = "100px"
        img.style.padding = "0 0 0 20px"
        div.append(img)
    }
}

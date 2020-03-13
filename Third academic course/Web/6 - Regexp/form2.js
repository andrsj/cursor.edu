const checkname = firstname =>{

    let test = false

    let filterFalse = [
        /\s[A-Za-z]\s/g,
        /(''){1}/,
        /\s'\s/g
    ]
    for (i of filterFalse){
        if (!i.test(firstname.value)){
            test = false
            break
        }
        else test = true
    }
    let filterTrue = [
        /^\s*([A-Z][a-z])/g,
        /\s([A-Za-z][a-z])/g
    ]
    for (i of filterTrue){
        if (!i.test(firstname.value)) test = true
        else {
            test = false
            break
        }
    }




    if ( test ) {
        firstname.style.border = "1px black solid";
        firstname.style.borderBottom = "2px red solid";
    }
    else{
        firstname.style.border = "1px black solid";
        firstname.style.borderBottom = "2px green solid";
    }
}

const checklastname = lastname => {
    // let filter = /^[A-Za-z]+(?:[\-'\s][A-Za-z]+){2,29}$/
    let filter = /^[A-Z]((\'[a-z])|(\-[a-zA-Z])|([a-z])){1,19}$/
    if ( !filter.test(lastname.value.replace(/\s/g, '')) ) {
        lastname.style.border = "1px black solid";
        lastname.style.borderBottom = "2px red solid";
    }
    else{
        lastname.style.border = "1px black solid";
        lastname.style.borderBottom = "2px green solid";
    }
}

const checkdate = date => {
    let filter = /^((0[1-9])|([12]\d)|(3[01]))[\./-]((0[1-9])|(1[012]))[\./-]((19\d\d)|(20[01]\d)|(\d\d))$/
    if ( !filter.test(date.value) ) {
        date.style.border = "1px black solid";
        date.style.borderBottom = "2px red solid";
    }
    else {
        date.style.border = "1px black solid";
        date.style.borderBottom = "2px green solid";
    }
}

const checkemail = email => {
    let filter = /^[a-z](([a-z\d_])|(\-[a-z\d_])|(\.[a-z\d_]))*[a-z\d]@([a-z\d]+\.[a-z\d]{1,10}){1,7}([a-z]{1,4})$/
    if ( !filter.test(email.value) ) {
        email.style.border = "1px black solid";
        email.style.borderBottom = "2px red solid";
    }
    else{
        email.style.border = "1px black solid";
        email.style.borderBottom = "2px green solid";
    }
}

const checklanguage = (arr) => {
    let iter = 0;
    for(i of arr){
        if(i.checked) iter += 1;
    }
    alert(`U knw ${iter} languages!!!`);
}

const checktext = text => {
    if(text.value.length > 500){
        alert("Багато тексту! Більше 500 символів");
        text.style.borderBottom = "2px solid red"
    } else {
        text.style.borderBottom = "2px solid green"
    }
}

const checkpass = (password, a = false) => {
    // let filter = /((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#])){6,15}/
    let filter = /((?=.*\d)(?=.*[a-z])(?=.*[A-Z])){6,15}/
    if ( !filter.test(password.value) ) {
        password.style.border = "1px black solid";
        password.style.borderBottom = "2px red solid";
    } else {
        password.style.border = "1px black solid";
        password.style.borderBottom = "2px green solid";
    }
    if(a){
        if (password.value != document.getElementById("pass2").value){
            document.getElementById("pass2").style.border = "1px black solid";
            document.getElementById("pass2").style.borderBottom = "2px red solid";
        } else {
            document.getElementById("pass2").style.border = "1px solid black";
            document.getElementById("pass2").style.borderBottom = "2px solid green";
        }
    }

}

const validate = () => {
    let firstname = document.getElementById("firstname"),
        lastname = document.getElementById("lastname"),
        date = document.getElementById("date"),
        email = document.getElementById("email"),
        password = document.getElementById("pass1"),
        languages = document.querySelectorAll("input[type='checkbox']");

    // console.table(languages,languages[0].checked);
    checkname(firstname);
    checklastname(lastname);
    checkdate(date);
    checkemail(email);
    checklanguage(languages);
    checkpass(password,true);
}
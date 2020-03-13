$(document).ready(function(){
    let block = $("#zadachi"), //Шукаєм блок з задачами
        buttons = block.children().children().children().children(".back").children("button"); //Шукаємо кнопки для відповідей
    var answers = ["100",[true,true,false,false],[false,true,false,false],["1","2"]], //Масив відповідей
        arrcheck = [], //Масив зачеканих користувачем чекбоксів
        arrradio = []; //Масив зачеканих користувачем радіокнопок

    for(let i=0; i<buttons.length; i++){ //Цикл надання атрибутів кожній кнопці для відповідей , щоб натискаючи на кнопку, для того, щоб ми могли звіряти введене користувачем з відповідною відповіддю в масиві
        buttons[i].setAttribute("data-index",i);
    }
    
    $("button").click(function(){ //Функція натискання кнопки
        let input = $(this).parent().children("input"); //Пошук інпутів (Текстбоксу)
        if (input.length == 0) //Якщо не знайдено, шукаємо їх в формі
        //Форма створення для того, щоб групувати чекбокси та радіокнопки
            input = $(this).parent().children().children("input"); //Сам пошук


        if (input.attr("type") == "text" && input.length == 1) //Якщо текстбокс один, то...
            if(input.val() == answers[$(this).attr("data-index")]) //Перевірка введених даних
                TrueAnswer(input.val() + " - true answer"); //Вивід правильної відповіді на центр екрану через функцію
            else
                FalseAnswer(input.val() + " - false answer"); //Вивід неправильної відповіді на центр екрану через функцію

        if (input.attr("type") == "checkbox"){ //Якщо знайдено чекбокси
            for(var i=0; i < input.length; i++){ //Вводимо дані, що вибрав користувач
                arrcheck[i] = input[i].checked; //Поелементно
            }
            if(arraysEquals(arrcheck,answers[$(this).attr("data-index")])) //Якщо порівняні дані однакові, то
                TrueAnswer("True"); //Виводимо "True" на центр екрану
            else
                FalseAnswer("False"); //Виводимо "False" на центр екрану
        }

        if (input.attr("type") == "radio"){ //Якщо знайдено радіокнопки 
            for(var i=0; i < input.length; i++){ //Вводимо дані, що вибрав користувач
                arrradio[i] = input[i].checked; //Поелементно
            }
            if(arraysEquals(arrradio,answers[$(this).attr("data-index")])) //Якщо порівняні дані однакові, то
                TrueAnswer("True"); //Виводимо "True" на центр екрану
            else
                FalseAnswer("False"); //Виводимо "False" на центр екрану
        }

        if (input.attr("type") == "text" && input.length == 2){ //Якщо знайдено ДВА (2) текстбокси, то...
            if(input[0].value == answers[$(this).attr("data-index")][0] &&
            input[1].value == answers[$(this).attr("data-index")][1]){ //Якщо обидва введених відповідей вірні, то...
                TrueAnswer("True"); //Виводимо "True" на центр екрану
            }
            else
                FalseAnswer("False"); //Виводимо "False" на центр екрану
        }

    })
})

function arraysEquals(arr1,arr2){ //Функція порівняння масивів
    if(arr1.length != arr2.length) return false; //Якщо масиви не рінві за розміром, завершуємо функцію з результатом false
    for (let i=0; i<arr1.length; i++){ // Цикл , що проходить по кожному елементу
        if(arr1[i] != arr2[i]) return false; //Якщо елементи з одного масиву, не такий же, як у другого, повертаємо результат функції false
    }
    return true; //Якщо все пройшло вдало - TRUE
}

function TrueAnswer(a){ //Функція, що виводить по середині правильну відповідь
    let block = $(".answer"); //Шукаємо блок, в який ми будемо виводити вдповідь
    block.children().text(a); //Виводимо відповідь в параграф нашого блоку
    block.css({"display":"block","background-color":"chartreuse"}); //Властивості CSS 1)Поаказати блок 2)Колір фону - зелений
    setTimeout(function(){
        block.css("display","none"); //Через 2,5 секунди встановити видимість блоку як none (приховати)
    },2500);
}

function FalseAnswer(a){ //Функція, що виводить по середині не правильну відповідь
    let block = $(".answer"); //Шукаємо блок, в який ми будемо виводити вдповідь
    block.children().text(a); //Виводимо відповідь в параграф нашого блоку
    block.css({"display":"block","background-color":"crimson"});  //Властивості CSS 1)Поаказати блок 2)Колір фону - червоний
    setTimeout(function(){
        block.css("display","none"); //Через 2,5 секунди встановити видимість блоку як none (приховати)
    },2500);
}
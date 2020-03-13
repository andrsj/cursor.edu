$(document).ready(function(){ // Якщо документ готовий, то
    var     inputs = $("input"), //Змінна інпутів (текстбокси, чекбокси, радіобатони)
            arrcheck = [], //Масив чЕкнутих чекбоксів
            arrradio = []; //Масив чЕкнутих радіобатонів
    const   answers = ["2","10000",[true,true,false,false],[false,false,false,true],["1","200"],["True","False"]], //Масив відповідей
            divs = $(".marketing").children("div"); //Блоки з задачами

    for(let i=0; i < divs.length; i++){ //Цикл для призначення кожній кнопці атрибуту
        var button = divs.children("div").children("button"); //Пошук кнопки в документі
        button[i].setAttribute("data-index",i); //Встановлення атрибуту
    }


    $("button").click(function() { //Функція при кліку на будь-яку кнопку
        let input = $(this).parent().children("input"); //Пошук інпутів
        if (input.length == 0) //Якщо інпут не знайдено, шукаємо інший
            input = $(this).parent().children().children("input"); //Пошук іншого

        if (input.attr("type") == "text" && input.length == 1) //Якщо знайдено один текстбокс
            alert(input.val() == answers[$(this).attr("data-index")] ? "True" : "False"); //Якщо правильно, то поверне ТРУ,  а якщо ні - фолсе)
        if (input.attr("type") == "checkbox"){ //Якщо знайдено чекбокси
            for(var i=0; i < input.length; i++){ //Цикл запису чЕків користувача
                arrcheck[i] = input[i].checked; //Запис поелементно
            }
            alert(arraysEquals(arrcheck,answers[$(this).attr("data-index")]) ? "True" : "False"); //Яещо правильно, то тру, ні - фолсе
            //Функція arraysEquals порівнює поелементно два масиви, тут вказано масив чЕків користувача і відповідних відповідей
        }

        if (input.attr("type") == "radio"){ //Якщо знайдено радіобатони
            for(var i=0; i < input.length; i++){ //Цикл запису чЕків радіобатонів
                arrradio[i] = input[i].checked; //Запис поелементно
            }
            alert(arraysEquals(arrradio,answers[$(this).attr("data-index")]) ? "True" : "False"); //Якщо правильно, то тру, якщо ні - фолсе
            //Функція arraysEquals порівнює поелементно два масиви, тут вказано масив чЕків користувача і відповідних відповідей
        }

        if (input.attr("type") == "text" && input.length == 2){ //Якщо знайдено ДВА текстбокси
            if(input[0].value == answers[$(this).attr("data-index")][0] &&
            input[1].value == answers[$(this).attr("data-index")][1]){ //ЯКЩО дві відповіді співпадають, то...
                alert("True");
            }
            else
                alert("False");
        }

    })
})

function arraysEquals(arr1,arr2){ //Функція порівняння масивів (приймає два масиви)
    if(arr1.length != arr2.length) return false; //Якщо масиви не рівні за розміром, то фолсе
    for (let i=0; i<arr1.length; i++){ // Цикл порівняння поелементно
        if(arr1[i] != arr2[i]) return false; // Якщо один з них не однаковий, функція завершується з значенням фолсе
    }
    return true; //якщо все пройшло добре, то ТРУ)
}
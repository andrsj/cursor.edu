var number1 = false,
    number2 = false,
    operation = "+",
    e = document.querySelector("input.input");

function getOper(input){
    number1 = parseFloat(e.value);
    operation = input;
    e.value = "";
}

function final(){
    let b = parseFloat(e.value);
    switch(operation){
        case "+":
            e.value = number1 + b;
            break;
        case "-":
            e.value = number1 - b;
            break;
        case "*":
            e.value = number1 * b;
            break;
        case "/":
            e.value = number1 / b;
            break;
    }
    number1 = false;
    number2 = false;
}
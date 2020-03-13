function select(a){
    console.table(a,a.nextElementSibling);
    console.log(a.options);
    let newOption = new Option('0','0');
    switch(a.selectedIndex){
        case 0:
            while (a.nextElementSibling.firstChild) {
                a.nextElementSibling.removeChild(a.nextElementSibling.firstChild);
            }
            massiveChars = genCharArray("a","g");
            for(let i = 0; i < massiveChars.length; i++){
                newOption = new Option(massiveChars[i], massiveChars[i]);
                a.nextElementSibling.append(newOption);
            }
            break;
        case 1:
            while (a.nextElementSibling.firstChild) {
                a.nextElementSibling.removeChild(a.nextElementSibling.firstChild);
            }
            massiveChars = genCharArray("h","n");
            for(let i = 0; i < massiveChars.length; i++){
                newOption = new Option(massiveChars[i], massiveChars[i]);
                a.nextElementSibling.append(newOption);
            }
            break;
        case 2:
            while (a.nextElementSibling.firstChild) {
                a.nextElementSibling.removeChild(a.nextElementSibling.firstChild);
            }
            massiveChars = genCharArray("o","u");
            for(let i = 0; i < massiveChars.length; i++){
                newOption = new Option(massiveChars[i], massiveChars[i]);
                a.nextElementSibling.append(newOption);
            }
            break;
        case 3:
            while (a.nextElementSibling.firstChild) {
                a.nextElementSibling.removeChild(a.nextElementSibling.firstChild);
            }
            massiveChars = genCharArray("v","z");
            for(let i = 0; i < massiveChars.length; i++){
                newOption = new Option(massiveChars[i], massiveChars[i]);
                a.nextElementSibling.append(newOption);
            }
            break;
    }
}

function genCharArray(charA, charZ) {
    var a = [], // massive
        i = charA.charCodeAt(0), //first element 
        j = charZ.charCodeAt(0); //last element
    for (; i <= j; ++i) {
        a.push(String.fromCharCode(i));
    }
    return a; //return massive
}
// genCharArray('a', 'z'); // ["a", ..., "z"]
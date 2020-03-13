function show(){
    var text = document.getElementsByTagName("input")[0];
    var checkboxes = document.getElementsByClassName('checkbox');
    var val = parseFloat(text.value);
    if (checkboxes[0].checked == true) {
        alert(val * val)
    }
    if (checkboxes[1].checked == true) {
        alert(val * val * Math.PI )
    }
    if (checkboxes[2].checked == true) {
        alert(val * val / 2)
    }
    if (checkboxes[3].checked == true) {
        alert(2 * Math.PI * val)
    }
    if (checkboxes[4].checked == true) {
        alert(Math.PI * val * val * val * 4 / 3)
    }
    // console.log(checkboxes)
    // alert(checkboxes[0].checked)
}
$(document).ready(function(){
    var carousel        = $(".carousel-inner"),
        wrapper         = carousel.children("div"),
        container       = wrapper.children("div"),
        caption         = container.children("div"),
        firstcollapse   = caption.children("div"),
        buttons         = firstcollapse.children("div").children("button"),
        secondcollapse  = firstcollapse.children("div").children("div"),
        answers         = secondcollapse.children("p"),
        answersOnQuestion = ["1","3","10","3","3","6","Так",[1,0,1,0],[1,1,0,0]],

        n = 0,
        arrayButtons       = [],
        buttonsId          = [];

    for(var i = 0; i < buttons.length; i++){
        arrayButtons.push(buttons[i]);
    }
    for(var j = 0; j < arrayButtons.length; j++){
        buttonsId.push(arrayButtons[j]["id"]);
    }

    $("button").click(function(){

        if($(this).attr("id") != undefined){
            var checkinputs = $(this).parent().parent().children("input[type='checkbox']");
            var checktextboxs = $(this).parent().parent().children("input[type='text']");
            for(var j = 0 ; j < buttonsId.length ; j++){
                if($(this).attr("id") == buttonsId[j]){
                    n = j;
                    break;
                }
            }
            
            if(checkinputs.length > 0){
                var checkedcheckboxes = [];
                for(var j=0; j<checkinputs.length; j++){
                    checkedcheckboxes.push(checkinputs[j].checked);
                }
                if(arrayIsarray(checkinputs,answersOnQuestion[n])){
                    console.log("True answer");
                }
                else{
                    console.log("False answer");
                }

            }
            if(checktextboxs.length > 0 && checktextboxs.length < 2){
                if(answersOnQuestion[n] == checktextboxs[0].value){
                    console.log("True answer");
                    $(".collapse_content").css({"color":"white", "background":"red", "opacity" : "1"});
                    $(".collapse_content").css({"color":"white", "background":"rgb(17,202,0)"});
                    $(answers[n]).text("Відповідь \"" + checktextboxs[0].value + "\" правильна");

                    timer();

                    checktextboxs[0].value = "";
                    $(".collapse_content").animate({
                        opacity: 0
                    },4500);
                    setTimeout(function(){
                        $(".collapse_content").removeClass("show");
                    },5000);
                }
                else{
                    if(checktextboxs[0].value == ""){
                        console.log("Empty answer");

                    }
                    else{
                        console.log("False answer");
                    }
                }
            }
            if(checktextboxs.length > 1){
                console.log("Have 2+ txtboxes");
            }
            
        }
    })
})

function arrayIsarray(arr1,arr2){
    var check;
    if(arr1.length == arr2.length){
        check = true;
        for(var i = 0; i<arr1.length; i++){
            if(arr1[i].checked != arr2[i]){
                check = false;
            }
        }
    }
    else{
        check = false;
    }
    return check;
}

function timer(){
    $(".timer").text("Time : "+ 5);
    setTimeout(function(){
        $(".timer").text("Time : "+ 4);
    },1000);
    
    setTimeout(function(){
        $(".timer").text("Time : "+ 3);
    },2000);
    
    setTimeout(function(){
        $(".timer").text("Time : "+ 2);
    },3000);
    
    setTimeout(function(){
        $(".timer").text("Time : "+ 1);
    },4000);

    setTimeout(function(){
        $(".timer").text("");
    },5000);
};
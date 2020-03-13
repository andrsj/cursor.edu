$(document).ready(function(){
    var answers  = ["1","3","10","3","3","6","Так",[1,0,1,0],[1,1,0,0],[6,"x-1"]],
        slides   = $(".carousel-inner").children();
        buttons  = slides.children().children().children().children().children("button"),
        paragraphs = slides.children().children().children().children().children().children(),
        counter = 0;
    
    for(let i = 0; i<slides.length; i++){
        buttons[i].setAttribute("test",i);
    }
    console.log(buttons);
    
    for(var i = 0; i<slides.length; i++){
        var button = buttons[i];
            paragraph = paragraphs[i];

        //console.log(button.hasAttribute("id"));
        //console.log(button.getAttribute("id"));

        button.setAttribute("data-index",i);
        paragraph.setAttribute("data-index",i);
    }

    // slides -> .carousel-item -> .container -> .carousel-caption ->
    // -> button + .collapse -> input + div -> button + .collapse -> p

    $("button").click(function(){

        for(var j = 0; j<slides.length; j++){
            if($(this).attr("data-index")==j){
                var item = $(this).parent("div").parent("div").children("input");

                // console.log(j);
                // console.log(this);
                // console.log($(this).parent("div"));
                // console.log($(this).parent("div").parent("div"));
                // console.log($(this).parent("div").parent("div").children("input"));
                // console.log($(this).parent("div").parent("div").children("input").val());

                if(item.attr("type") == "checkbox"){
                    var checkedcheckboxes = [];
                    for(var n=0; n<item.length; n++){
                        checkedcheckboxes.push(item[n].checked);
                    }
                    if(arrayIsarray(item,answers[j])){
                        $(".collapse_content").css({"color":"white", "background":"red", "opacity" : "1"});
                        $(".collapse_content").css({"color":"white", "background":"rgb(17,202,0)"});
                        $(paragraphs[j]).text("Відповідь правильна");
                        counter++;
                        timer();
                        $(".collapse_content").animate({
                            opacity: 0
                        },4500);
                        setTimeout(function(){
                            $(".collapse_content").removeClass("show");
                        },5000);
                    }
                    else{
                        $(".collapse_content").css({"color":"white", "background":"rgb(255, 65, 65)", "opacity" : "1"});
                        $(paragraphs[j]).text("Відповідь не правильна!");
                        timer();
                        $(paragraphs[j]).focus();
                        $(".collapse_content").animate({
                            opacity: 0
                        },4500);
                        setTimeout(function(){
                            $(".collapse_content").removeClass("show");
                        },5000);
                    }
                }
                else{
                    if(item.length == 1){
                        if(item.val() == answers[j]){
                            $(".collapse_content").css({"color":"white", "background":"red", "opacity" : "1"});
                            $(".collapse_content").css({"color":"white", "background":"rgb(17,202,0)"});
                            $(paragraphs[j]).text("Відповідь \"" + item.val() + "\" правильна");
                            counter++;
                            timer();
                            item.val("");
                            $(".collapse_content").animate({
                                opacity: 0
                            },4500);
                            setTimeout(function(){
                                $(".collapse_content").removeClass("show");
                            },5000);
                        }
                        else{
                            if(item.val() == "") {
                                $(".collapse_content").css({"color":"white", "background":"rgb(255, 65, 65)", "opacity" : "1"});
                                $(paragraphs[j]).text("Відповідь не задана!");
                                timer();
                                $(paragraphs[j]).focus();
                                $(".collapse_content").animate({
                                    opacity: 0
                                },4500);
                                setTimeout(function(){
                                    $(".collapse_content").removeClass("show");
                                },5000);
                            }
                            else {
                                $(".collapse_content").css({"color":"white", "background":"rgb(255, 65, 65)", "opacity" : "1"});
                                $(paragraphs[j]).text("Відповідь \"" + item.val() + "\" не правильна");
                                timer();
                                item.val("");
                                $(".collapse_content").animate({
                                    opacity: 0
                                },4500);
                                setTimeout(function(){
                                    $(".collapse_content").removeClass("show");
                                },5000);
                            }
                        }
                    }
                    else{
                        if(item[0].value == answers[j][0] && item[1].value == answers[j][1]){
                            $(".collapse_content").css({"color":"white", "background":"red", "opacity" : "1"});
                            $(".collapse_content").css({"color":"white", "background":"rgb(17,202,0)"});
                            $(paragraphs[j]).text("Відповідь правильна");
                            counter++;
                            timer();
                            $(".collapse_content").animate({
                                opacity: 0
                            },4500);
                            setTimeout(function(){
                                $(".collapse_content").removeClass("show");
                            },5000);
                        }
                        else{
                            $(".collapse_content").css({"color":"white", "background":"rgb(255, 65, 65)", "opacity" : "1"});
                                $(paragraphs[j]).text("Відповідь не правильна");
                                timer();
                                $(".collapse_content").animate({
                                    opacity: 0
                                },4500);
                                setTimeout(function(){
                                    $(".collapse_content").removeClass("show");
                                },5000);
                        }
                    }
                }
                console.log(counter);
            }
        }
    })
});


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
};
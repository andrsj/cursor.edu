$(document).ready(function(){
    var inputs = ["#one_input","#two_input","#three_input","#four_input","#five_input","#six_input","#seven_input"];
    var answers = ["#one_answer","#two_answer","#three_answer","#four_answer","#five_answer","#six_answer","#seven_answer"];
    var buttons = ["#one","#two","#three","#four","#five","#six","#seven"];
    var answersonquestion = ["1","3","10","3","3","6","Так"];
    var n = 0;

    $("button").click(function(){
        if($(this).attr("id") == "one"){n = 0}
        if($(this).attr("id") == "two"){n = 1}
        if($(this).attr("id") == "three"){n = 2}
        if($(this).attr("id") == "four"){n = 3}
        if($(this).attr("id") == "five"){n = 4}
        if($(this).attr("id") == "six"){n = 5}
        if($(this).attr("id") == "seven"){n = 6}

        if($(this).attr("id") != undefined){
            $(".collapse_content").css("opacity");
            if($(inputs[n]).val()==answersonquestion[n])
            {
                $(".collapse_content").css({"color":"white", "background":"red", "opacity" : "1"});
                $(".collapse_content").css({"color":"white", "background":"rgb(17,202,0)"});
                $(answers[n]).text("Відповідь \"" + $(inputs[n]).val() + "\" правильна");

                timer();

                $(inputs[n]).val("");
                $(".collapse_content").animate({
                    opacity: 0
                },4500);
                setTimeout(function(){
                    $(".collapse_content").removeClass("show");
                },5000);
            }
            else
            {
                if($(inputs[n]).val() == "") {
                    $(".collapse_content").css({"color":"white", "background":"rgb(255, 65, 65)", "opacity" : "1"});
                    $(answers[n]).text("Відповідь не задана!");
                    timer();
                    $(inputs[n]).val("");
                    $(inputs[n]).focus();
                    $(".collapse_content").animate({
                        opacity: 0
                    },4500);
                    setTimeout(function(){
                        $(".collapse_content").removeClass("show");
                    },5000);
                }
                else {
                    $(".collapse_content").css({"color":"white", "background":"rgb(255, 65, 65)", "opacity" : "1"});
                    $(answers[n]).text("Відповідь \"" + $(inputs[n]).val() + "\" не правильна");
                    timer();
                    $(inputs[n]).val("");
                    $(".collapse_content").animate({
                        opacity: 0
                    },4500);
                    setTimeout(function(){
                        $(".collapse_content").removeClass("show");
                    },5000);
                }
            }
        }
        
    });

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

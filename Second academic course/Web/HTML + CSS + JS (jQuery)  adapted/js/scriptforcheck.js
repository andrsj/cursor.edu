$("#nine").click(function(){
    if($("input#lol1").prop("checked") && $("input#lol2").prop("checked")){
        $(".nine_answers").css({"color":"white","background-color":"rgb(17,202,0)"});
        $("#nine_answer").text("True");
    }
    else{
        $(".nine_answers").css({"color":"white","background-color":"rgb(255, 65, 65)"});
        $("#nine_answer").text("False");
    }
});
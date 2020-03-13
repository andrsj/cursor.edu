var tabs_content = $(".tabs_content");
var tabs = $(".tab");
$(".tabs_content").hide();
$(tabs_content[0]).show();

// $(tabs).click(function(){
//     switch(this){
//         case tabs[0]:
//             $(tabs_content).hide();
//             $(tabs_content[0]).show();
//             break;
//         case tabs[1]:
//             $(tabs_content).hide();
//             $(tabs_content[1]).show();
//             break;
//         case tabs[2]:
//             $(tabs_content).hide();
//             $(tabs_content[2]).show();
//             break;
//     }
// });

$(tabs).click(function(){
    for(var i=0; i < tabs.length; i++){
        if(this == tabs[i]){
            $(tabs_content).hide();
            $(tabs_content[i]).show();
        }
    }
});
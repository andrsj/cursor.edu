const toggled = () => {
    $(".text-query").toggle();
}
const bolded = () => {
    if($(".text-query").css("font-weight") != 700)
        $(".text-query").css("font-weight","bold")
    else
        $(".text-query").css("font-weight","normal")
}

function getRandomInt(max) {
    return Math.floor(Math.random() * Math.floor(max));
}

const colored = () => {
    $(".text-query").css("color","rgb(" + getRandomInt(256) + "," + getRandomInt(256) + "," + getRandomInt(256) + ")")
}

const animated = () => {
    console.log($(".lol-query").css("width"), $(".lol-query").css("height"))
    let w = $(".lol-query").width() * 1.5,
        h =  $(".lol-query").height() * 1.5;
    console.log(w,h);
    $(".lol-query").animate({
        width: w + "px",
        height: h + "px"
    } , 100)
}

const moved = () => {
    $(".block-query").animate({
        left: "+=10px",
        top: "+=10px"
    }, 100)
}

const animeover = () => {
    let img = $("#img")
    img.animate({left: "100%"},"slow")
}
const animeout = () => {
    let img = $("#img")
    img.animate({left: 100},"slow")
}

const change = () => {
    let op = $("#img").css("opacity")
    if (op == "0"){
        $("#img").css("opacity","1")
        return
    }
    op -= 0.1
    $("#img").css("opacity",op)
}

const changetable = () => {
    $("tr:even").css("color","blue")
    $("tr:odd").css("color","yellow")
    $("td:last").css("color","red")
}

$( function () {
    let words = [
        "Audi",
        "Apple",
        "Alfa Romeo",
        "Aston Martin",

        "Cherry",
        "Chevrolet",
        "Citroen",
        "Chrysler",
        "Cupra",

        "Lamba",
        "Landrover",
        "Lexus",
        "Lincoln",
        "Lancia",

        "Pagani",
        "Porsche",
        "Peugeot",
        "Porsche911",

        "Range Rover",
        "Renault",
        "Rolls-Royce",
    ]
    $("#auto").autocomplete(
    {
        source: words,
        autoFill: true,
        appendTo: "#List"
    }
    )
})
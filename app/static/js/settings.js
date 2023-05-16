const tabBtn = document.querySelectorAll(".tab");
const tab= document.querySelectorAll(".tabShow");

function tabs(panelIndex) {
tab.forEach(function(node) {
    node.style.display= "none";
});
tab[panelIndex].style.display ="block";
}
tabs(0);

$(".tab").click(function() {
    $(this).addClass("active").siblings().removeClass("active");
})

let colourInput = document.getElementById('primColour');
let colourInput2= document.getElementById('secoColour');
let textColour = document.getElementById('textColour')

// Whenever the user changes the color, the input event will be called.
colourInput.addEventListener('input', () =>{
    document.getElementById("topPage").style.backgroundImage = "linear-gradient(225deg ," + colourInput.value+" 50%," + colourInput2.value +" 90%)";
    document.getElementById("botPage").style.backgroundImage = "linear-gradient(225deg ," + colourInput2.value+" 50%," + colourInput.value +" 90%)";
});
colourInput2.addEventListener('input', () =>{
    document.getElementById("topPage").style.backgroundImage = "linear-gradient(225deg ," + colourInput2.value+" 50%," + colourInput.value +" 90%)";
    document.getElementById("botPage").style.backgroundImage = "linear-gradient(225deg ," + colourInput.value+" 50%," + colourInput2.value +" 90%)";
});

textColour.addEventListener('input', () =>{
    var elements = document.querySelectorAll('h1, div');
    for (var x = 0; x < elements.length; x++)
        elements[x].style.color = textColour.value;
})
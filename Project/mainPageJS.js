function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
    document.body.style.backgroundColor = "rgba(0,0,0,1)";
  }
  
function closeNav() {
document.getElementById("mySidenav").style.width = "0";
document.getElementById("main").style.marginLeft= "0";
document.body.style.backgroundColor = "white";
}

function insertText() {
    let theText = document.getElementById("insertText").value;
    if(theText != ''){
        document.getElementById("insertText").value = "";
        let theTextSet = document.createElement("p");
        theTextSet.innerText="Tony: "+theText;
        document.getElementById("textMessage").appendChild(theTextSet);
    }
}

function enterInsert(){
    if(event.key === 'Enter') {
        insertText();        
    }
}
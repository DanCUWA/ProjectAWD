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
function toggleNav(){ 
    if (document.getElementById("mySidenav").style.width == "250px") { 
        closeNav(); 
    } else { 
        openNav(); 
    }
}
//___________________________________________________________
// Message Box
const textarea = document.querySelector("#insertText");
textarea.addEventListener("keyup", e =>{
  textarea.style.height = "0px";
  let scHeight = e.target.scrollHeight;
  textarea.style.height = `${scHeight}px`;
});

const form = document.querySelector("#input")
const output = document.querySelector("#textMessage")


form.addEventListener("submit", e =>{
  e.preventDefault();
  insertText()
});

textarea.addEventListener("keydown", e =>{
  if(e.keyCode == 13 && !e.shiftKey){
    e.preventDefault();
    insertText()
  }
})

function insertText() {
  const formData = new FormData(form); // create new FormData object from form data
  const myInputValue = formData.get('myInput'); // get value of myInput field
  if(myInputValue != ''){
    let theTextSet = document.createElement("p");
    theTextSet.innerText="Tony: "+myInputValue;
    output.appendChild(theTextSet);
    output.scrollTop =  output.scrollHeight - output.clientHeight;
  }

  textarea.value = ''; // clear the textarea value
}
//___________________________________________________________

// function insertText() {
//     let theText = document.getElementById("insertText").value;
//     if(theText != ''){
//         document.getElementById("insertText").value = "";
//         let theTextSet = document.createElement("p");
//         theTextSet.innerText="Tony: "+theText;
//         let textMessage = document.getElementById("textMessage");
//         textMessage.appendChild(theTextSet);
//         textMessage.scrollTop =  textMessage.scrollHeight - textMessage.clientHeight;
//     }
// }

// function enterInsert(){
//     if(event.key === 'Enter') {
//         insertText();        
//     }
// }
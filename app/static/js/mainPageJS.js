function colorChange(primColor, secoColor, textColor) {
  const root = document.querySelector(":root");
  root.style.setProperty('--primary-color', primColor);
  root.style.setProperty('--secondary-color', secoColor);
  root.style.setProperty('--text-color', textColor);
  console.log(primColor);
}

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

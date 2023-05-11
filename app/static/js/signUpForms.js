let sform = document.querySelector("#signup");
sform.addEventListener('submit', (event) => { 
  event.preventDefault();
  let err = 0;
  let it = 0; 
  //User,email,pass
  let info = [];
  Array.from(sform.elements).filter(el => el.type != "submit").forEach((el) => {
    console.log(el.value);
    if (el.value == ""){
      el.style.borderColor = "red"; 
      err++;
    } else { 
      el.style.borderColor = "grey"; 
      if (it == sform.elements.length - 1){ 
        if (el.value != info[2]){ 
          el.style.borderColor = "red"; 
          err++;
        }
      } else { 
        info[it++] = el.value; 
        el.value = ""; 
      }
    } 
  });
  if (err > 0){ 
    //Write an error message
  }
  info.forEach(el=>{ 
    console.log(el);
  })
});

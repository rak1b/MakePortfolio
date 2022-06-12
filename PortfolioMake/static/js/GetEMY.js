const getE= (elm)=>{
  let el = document.querySelectorAll(elm)
    if(el.length > 1){
          return el;
      }else if(el.length == 1){
          return el[0];}
      else return []
  }

console.log("Get me loaded");
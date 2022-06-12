

  const heroEditbtn = document.getElementById("edit_hero_btn");
  const heroEdit = document.getElementById("hero_edit");

  const hero_show_hide = () => {
    console.log("Hero edit clicked...");
    heroEdit.classList.toggle("element_show");
  };

  const _= (elm)=>{
    let el = document.querySelectorAll(elm)
    if(el.length > 1){
          return el;
      }else if(el.length == 1){
          return el[0];}
      else return []
  }
  
//   console.log("testing")
//   const getE= (elm)=>{
//   let el = document.querySelectorAll(elm)
//     if(el.length > 1){
//           return el;
//       }else if(el.length == 1){
//           return el[0];}
//       else return []
//   }
  
//   console.log("testing")
//   console.log(getE(".landing_text"))

//   const LoginState = {
//     which : "signup"
//   }

//   const SetLoginState =(val)=>{
//     LoginState.which = val
//   }

//   const toggleLoginSignUp = ()=>{

//     if (LoginState.which === 'signup') {
//       // getE("#loginForm").classList.add("hide")
    
//       getE("#signupForm").classList.toggle("show")
//     }
    
//     if (LoginState.which === 'login') {
//       getE("#loginForm").classList.toggle("show")
    
//       // getE("#signupForm").classList.add("hide")
//     }
    
//     }
    

// console.log(getE("#openSignup"));
//   getE("#openSignup").onclick=(e)=>{
//     console.log("open signup clicked");
//     console.log(LoginState.which);

//     e.preventDefault()
//     SetLoginState("signup")
//     toggleLoginSignUp()

//   }


//   getE("#openLogin").onclick=(e)=>{
//     console.log("open Login clicked");
//     console.log(LoginState.which);

//     e.preventDefault()
//     SetLoginState("login")
//     toggleLoginSignUp()


//   }







// // signupForm


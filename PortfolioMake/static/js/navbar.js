const button_func = ()=>{
    console.log('Helloo')
    const menu_btn =  document.getElementById("mybtn");
    const back =  document.getElementById("back");
    menu_btn.classList.toggle('is-active');
    const phone_nav = document.getElementById("phone_nav");
    if ( menu_btn.classList.contains('is-active') ){
        // menu_btn.classList.toggle('MyClass');
        console.log("is-active")
        phone_nav.classList.add('menu_show');
        phone_nav.classList.remove('menu_hide');
        // back.classList.add('filter_6px')
    }else{
        phone_nav.classList.remove('menu_show');
        phone_nav.classList.add('menu_hide');
        // back.classList.remove('filter_6px')

    }

}



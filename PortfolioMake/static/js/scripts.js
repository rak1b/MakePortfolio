const heroEditbtn = document.getElementById("edit_hero_btn");
const heroEdit = document.getElementById("hero_edit");

const hero_show_hide = () => {
  console.log("Hero edit clicked...");
  heroEdit.classList.toggle("element_show");
};

const show_hide = (id) => {
  console.log("in show hide///////////////////");
  console.log(id);
  const elem = document.getElementById(id);

  console.log("Hero edit clicked...");
  elem.classList.toggle("element_show");
};

const hide_then_show = (id) => {
  console.log("hide_then_show");
  const elem = document.getElementById(id);
  elem.classList.toggle("element_hide");
};

const show = (id) => {
  const elem = document.getElementById(id);
  elem.classList.remove("element_hide");
};

const normalShow=(id)=>{
  const elem = document.getElementById(id);
  elem.classList.toggle("hide");
}
 
const openMore = (id)=>{
  const more = 'more_'+id;
  const options = 'options_'+id
  // console.log(more);
  // console.log(options);
  normalShow(options)

}

const update_project_info = (project_container_id,project_id)=>{

  show_hide(project_container_id)
  
}
const _ = (elm) => {
  let el = document.querySelectorAll(elm);
  if (el.length > 1) {
    return el;
  } else if (el.length == 1) {
    return el[0];
  } else return [];
};

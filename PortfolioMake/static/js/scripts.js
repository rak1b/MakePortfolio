const heroEditbtn = document.getElementById("edit_hero_btn");
const heroEdit = document.getElementById("hero_edit");

const hero_show_hide = () => {
  console.log("Hero edit clicked...");
  heroEdit.classList.toggle("element_show");
};

const show_hide = (id,resetForm) => {
  console.log("in show hide///////////////////");
  if(resetForm){
    $("#project_Form")[0].reset();
  }
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
  console.log(project_id);
  $.ajax({
    url: $("#update_project").attr("data-url"),
    method: "POST",
    data: {
      id: project_id,
      csrfmiddlewaretoken:document.getElementsByName("csrfmiddlewaretoken")[0].value,
      // csrfmiddlewaretoken:"{{csrf_token}}",
    },
    success: (res) => {
      console.log(res);
      data = res.data;
      $("#update_project_id").val(data.id);
      $("#project_title").val(data.title);
      $("#upload_container_img").attr(
        "src",
        `http://127.0.0.1:8000/media/${data.image}`
      );
      $("#short_description").val(data.short_description);
      // $("#full_description").html(data.full_description);
      $('.fr-element')[0].innerHTML = data.full_description
    },
    error: (err) => {
      console.log(err);
    },
  });
  
}

const changeCssVarColor = (var_name,colorInput)=>{

  const r = document.querySelector(':root');
  console.log(var_name);
  // console.log('#'+$(colorInput));
  console.log($('#'+colorInput).val());
  r.style.setProperty(var_name, $('#'+colorInput).val());
}
const changeCssVarColorFromDjango = (var_name,colorInput)=>{
  const r = document.querySelector(':root');
  r.style.setProperty(var_name, colorInput);
  // r.style.setProperty(var_name, $('#'+colorInput).val());
}
// changeCssVarColorFromDjango('--navy-dark','red')
// var r = document.querySelector(':root');
// r.style.setProperty('--navy-dark','green');
// r.style.setProperty('--white', 'red');


const updateTheme = ()=>{
  console.log("update theme working-----------------");
  console.log($("#theme_form").attr("data-url"));
  const color1 = $('#color1').val()
  const color2 = $('#color2').val()
  const color3 = $('#color3').val()
  data = {
    color1:color1,
    color2:color2,
    color3:color3,
    csrfmiddlewaretoken:document.getElementsByName("csrfmiddlewaretoken")[0].value,

  }
  $.ajax({
    url: $("#theme_form").attr("data-url"),
    method: "POST",
    data: data,
    success: (res) => {
      console.log(res);
    },
    error: (err) => {
      console.log(err);
    },
  });
}


const ImagePreview = (hiddenImageInput,ImagePlaceHolder,PreviewImage)=>{
  console.log('Image changed');
  const image = document.getElementById(hiddenImageInput)
  const img_placeholder = document.getElementById(ImagePlaceHolder)
  const previewImage = document.getElementById(PreviewImage)
  const file = image.files[0];
  img_placeholder.innerHTML =file.name
  img_placeholder.classList.add('edit_img_placeholder')
  previewImage.src=URL.createObjectURL(file)
  console.log(image.files[0]);


}


const PdfPreview = (hiddenImageInput,ImagePlaceHolder,PreviewImage)=>{
  console.log('pdf changed');
  const pdf = document.getElementById(hiddenImageInput)
  const pdf_placeholder = document.getElementById(ImagePlaceHolder)
  const preview_pdf = document.getElementById(PreviewImage)
  const pdf_file = pdf.files[0];
  pdf_placeholder.innerHTML =pdf_file.name
  pdf_placeholder.classList.add('edit_img_placeholder')

}


const _ = (elm) => {
  let el = document.querySelectorAll(elm);
  if (el.length > 1) {
    return el;
  } else if (el.length == 1) {
    return el[0];
  } else return [];
};

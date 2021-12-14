var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}

var nav = document.getElementById('nav');

      window.onscroll = function () {

        if(window.pageYOffset > 100){

         nav.style.position = "fixed";
         nav.style.top = 0;

         }else{
           // nav.style.position = "absolute";
           nav.style.position = 'relative'; //fixed
           nav.style.top = 100;
         }
      }


      inputTextToSave.value = localStorage.getItem('inputTextToSave');
      inputTextToSave.oninput = () => {
        localStorage.setItem('inputTextToSave', inputTextToSave.value)
      };

function compile() {
  var html = document.getElementById("html");
  var css = document.getElementById("css");
  var js = document.getElementById("js");
  var code = document.getElementById("code").contentWindow.document;

  document.body.onkeyup = function() {
    code.open();
    code.writeln(
      html.value +
        "<style>" +
        css.value +
        "</style>" +
        "<script>" +
        js.value +
        "</script>"
    );
    code.close();
  };
}

compile();
//use same function to load different types of html into the intial boxes to 'build' web pages.
var textareas = document.getElementsByTagName('textarea');
 var count = textareas.length;
 for(var i=0;i<count;i++){
     textareas[i].onkeydown = function(e){
         if(e.keyCode==9 || e.which==9){
             e.preventDefault();
             var s = this.selectionStart;
             this.value = this.value.substring(0,this.selectionStart) + "\t" + this.value.substring(this.selectionEnd);
             this.selectionEnd = s+1;
         }
     }
 }
 //kyles code, fixes tab.

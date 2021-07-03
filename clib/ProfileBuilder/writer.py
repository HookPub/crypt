html = """

<style>
  ul {
    list-style-type: none;
    margin: auto;
    padding: 0;
    overflow: hidden;
    background-color: #333;
    max-width: 720px;
    width: 50%;
  }

  li {
    float: left;
  }

  li a {
    display: block;
    color: white;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
  }
  li a:hover {
    background-color: #111;
  }

  .container {
    position: relative;
   text-align: center;
    color: black;
    padding: 1px;
  }

  .centered {
    position: absolute;
    top: 25%;
    left: 50%;
    transform: translate(-50%, -50%);
  }

  .warning {
    color: white;
  }

  body {
   background-image: url("../../src/bg.png");
  }

</style>
<script>
  function Write(variable) {
    document.write(variable);
}

//About bullets
var ab1 = "- Line about yourself -";
var ab2 = "- Line about yourself -"
var ab3 = "- Line about yourself -"
var ab4 = "- Line about yourself -"


</script>
<p3 class="warning"> If you dont know what this is, leave. </p3>


<div align="center">
  <img src="../../src/header.png">
  </div>

<br> </br>

  <ul>
    <li><a href="../../clib.html">Crypt Library.</a></li>
    <li><a href="../../cres.html">Crypt Resources.</a></li>
    <li><a href="../../index.html">Crypt Home.</a></li>
    <li><a href="../../cwp/index.html">Crypt Writer.</a></li>
    <li style="float:right"><a class="active" href="../../src/subguide.txt">Submission Guide .</a></li>
  </ul>

<br></br>

<h1 class="warning" align="center"> Name. </h1>

  <div align="center" class="container">
   <img src="../../src/middiv.png">
   <div class="centered">   <h1> About Me: </h1>  <p>  <script>Write(ab1)</script> </p> <p>  <script>Write(ab2)</script> </p> <p>  <script>Write(ab3)</script> </p> <p>  <script>Write(ab4)</script> </p>
 </div>
<br> </br>
 <div align="center" class="container">
  <img src="../../src/syndiv.png">
  <div class="centered">   <h1> Writings: </h1> <p> <a href="../usrcontnt/prt.txt"> Example writing </a> </p>
</div>

<h1 class="warning"> or you can host images, audio, video, or what ever else you want. </h1>

"""

f = open("NewWriterP.html", "a")
f.write(html)
print("Done")
f.close()

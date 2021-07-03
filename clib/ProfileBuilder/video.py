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

  .vtitle {
    color: white;
    font-size: 35px;
    -webkit-text-stroke-width: 1px;
  -webkit-text-stroke-color: red;
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


<h1 class="warning" align="center"> Monkey mans videos. </h1>

<div align="center">
<video width="500" height="500" controls>
  <source src="../../clib/usrcontnt/tstvid.mp4" type="video/mp4">
</video>
</div>
<p align="center" class="vtitle"> Monkey in the wild ^ </p>

<h1 align="center" class="warning"> or you can host images, audio, video, or what ever else you want. </h1>

"""

f = open("NewVideoP.html", "w")
f.write(html)
print("Done")
f.close()

const time = new Date().getHours();
let greeting;
if (time < 11) {
  greeting = "Good morning, Western Man.";
}
else if (time > 11 > 15) {
  greeting = "Good afternoon, Western Man.";
}
else {
  greeting = "Good Evening, Western Man.";
}
document.getElementById("greeting").innerHTML = greeting;

// ^ Index greeter

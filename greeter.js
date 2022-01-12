const time = new Date().getHours();
let greeting;
if (time < 11) {
  greeting = "Good morning, Western Man.";
}
else if (time > 11) {
  greeting = "Good afternoon, Western Man.";
}
else if (time < 15) {
  greeting = "Good Evening, Western Man.";
}
else {
  greeting = "Hello, Western Man.";
}
document.getElementById("greeting").innerHTML = greeting;

// ^ Index greeter

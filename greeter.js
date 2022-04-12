const time = new Date().getHours();
let greeting;
if (time < 12) {
  greeting = "Good morning, Western Man.";
}
else if (time < 17) {
  greeting = "Good afternoon, Western Man.";
}
else {
 wgreeting = "Good evening, Western Man.";
}

document.getElementById("greeting").innerHTML = greeting;

// ^ Index greeter

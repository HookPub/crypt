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

const wtime = new Date().getHours();
let wgreeting;
if (time < 11) {
  wgreeting = "Good morning, Western Man. Ready to write?";
}
else if (time > 11) {
  wgreeting = "Good afternoon, Western Man. Time to work.";
}
 else {
  wgreeting = "Ready to write, Western Man?";
}
document.getElementById("wgreeting").innerHTML = wgreeting;

//Writer Greeter

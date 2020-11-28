document.addEventListener("DOMContentLoaded", function() {
  var x = document.getElementById("student");
    var y = document.getElementById("teacher");
    var z = document.getElementById("btn");

    document.querySelector("#teacher").onclick = function() {
        console.log("Hello from teacher");
        x.style.left= "-400px";
        y.style.left= "50px";
        z.style.left= "110px";
    }
    document.querySelector("#student").onclick = function() {
        console.log("Hello");
        x.style.left= "50px";
        y.style.left= "450px";
        z.style.left= "0";
    }
});

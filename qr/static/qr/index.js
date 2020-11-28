document.addEventListener("DOMContentLoaded", function() {
    var x = document.getElementById("student");
    var y = document.getElementById("teacher");
    var z = document.getElementById("btn");
    function teacher(){
        x.style.left= "-400px";
        y.style.left= "50px";
        z.style.left= "110px";
    }
    function student(){
        x.style.left= "50px";
        y.style.left= "450px";
        z.style.left= "0";
    }
});
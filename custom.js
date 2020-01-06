function collapse() {
    var x = document.getElementById("nav-itens");
    if (x.style.display === "block") {
      x.style.display = "none";
    } else {
      x.style.display = "block";
    }
    var x = document.getElementById("main-logo");
    x.style.display = "none";
  }
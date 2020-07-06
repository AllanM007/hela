function switchSheet() {
    let theme = document.getElementById("theme");
  
    if (theme.getAttribute("href") == "static/light-mode.css") {
      theme.href = "static/dark-mode.css";
    } else {
      theme.href = "static/light-mode.css";
    }
  }
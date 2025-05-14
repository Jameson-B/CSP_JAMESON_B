let figure = document.getElementById("hoverable-figure")
let img = document.querySelector("#hoverable-figure img");
let caption = document.querySelector("#hoverable-figure figcaption")

function swapFigureOnEnter() {
    img.src = "https://images.unsplash.com/photo-1662925429325-cd579a0a8ff1?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D";
    img.alt = "Snowboarder in midair at Brighton Ski Resort in Utah";
    caption.innerHTML = '<p>A snowboarder mid-jump</p><p>Photo by <a href = "https://unsplash.com/@bariceric" target = "_blank" rel = "noopener">Eric Barrett</a> on <cite><a href = "https://unsplash.com/photos/a-person-jumping-in-the-air-on-a-snowboard-4RPWDdVdgAQ" target = "_blank" rel = "noopener">Unsplash</a></cite></p>';
}

function resetFigureOnLeave() {
    img.src = "https://images.unsplash.com/photo-1662925440167-7d4a36a0f721?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D";
    img.alt = "Snowboarder about to go off jump at Brighton Ski Resort in Utah";
    caption.innerHTML = ' <p>A snowboarder prepares to make a jump in the terrain park</p><p>Photo by <a href = "https://unsplash.com/@bariceric" target = "_blank" rel = "noopener">Eric Barrett</a> on <cite><a href = "https://unsplash.com/photos/a-person-lying-on-the-snow-zpaQ3A6QsZU" target = "_blank" rel = "noopener">Unsplash</a></cite></p>';
}

let button = document.getElementById("collapsible-button");
let content = document.getElementById("collapsible-content");

function showHideContent() {
    if (content.style.display === "none") {
        button.textContent = "Hide";
        content.style.display = "block";
    } else {
        button.textContent = "Show";
        content.style.display = "block"
    }
}
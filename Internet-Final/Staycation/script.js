function swapFigureOnEnter() {
    const img = document.querySelector(".card-container #hoverable-figure img");
    const caption = document.querySelector(".card-container #hoverable-figure figcaption");

    img.src = "https://images.unsplash.com/photo-1662925429325-cd579a0a8ff1?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D";

    caption.textContent = "A snowboarder mid-jump";
}

/*
<img class = "img-two" src = "https://images.unsplash.com/photo-1662925429325-cd579a0a8ff1?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                        alt = "Snowboarder in midair at Brighton Ski Resort in Utah"></img>

<figcaption class = "caption-two">
                            <p>A snowboarder mid-jump</p>
                            <p>Photo by <a href = "https://unsplash.com/@bariceric" target = "_blank" rel = "noopener">Eric Barrett</a> on <cite><a href = "https://unsplash.com/photos/a-person-jumping-in-the-air-on-a-snowboard-4RPWDdVdgAQ" target = "_blank" rel = "noopener">Unsplash</a></cite></p>
                        </figcaption>
*/
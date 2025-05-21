function show_hide(){
    if (document.getElementById("page-info-wrapper").style.display === "none") {
        document.getElementById("page-info-wrapper").style.display = "block"
        document.getElementById("page-info-button").innerHTML = "Show less"
    } else {
        document.getElementById("page-info-wrapper").style.display = "none"
        document.getElementById("page-info-button").innerHTML  = "Show more"
    }  
}
console.log("Script loaded")
let revealed = false
function show_hide(){
    if (revealed == false) {
        document.getElementById("hidden-paragraph").style.display = "block"
        revealed = true
    } else {
        document.getElementById("hidden-paragraph").style.display = "none"
        revealed = false
    }
    
}
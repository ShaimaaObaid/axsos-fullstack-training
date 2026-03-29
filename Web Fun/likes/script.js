/*let count =[9,12];
function likePost(){
    count++;
    document.querySelector(".likes").innerText= count +" like(s)"
}*/
const buttons = document.querySelectorAll(".likeButton");

buttons.forEach(button => { button.addEventListener("click", () => {
        const likesElem = button.parentElement.querySelector(".likes");
        let currentLikes = parseInt(likesElem.innerText);
        currentLikes++;
        likesElem.innerText = currentLikes + " like(s)";
    });
});
//change the name to shaymaa obaid when we click the edit profile
const editProfileLink = document.querySelector(".child3 a");
editProfileLink.addEventListener("click", function(e) {
    e.preventDefault(); // prevent the page to load so the name stay
    document.querySelector(".child2 h1").innerText = "Shaymaa Obaid";
});

const requestButtons = document.querySelectorAll(".Divv .true, .Divv .false");
const requestsCount = document.querySelector(".circle p");
const connectionsCount = document.querySelector(".secCircle p");

requestButtons.forEach(button => {
  button.addEventListener("click", function() {
    // when we click on accept remove the user from the request list
    const parentDiv = this.parentElement;
    parentDiv.remove();

        // decrease connection requests number

    let currentRequests = parseInt(requestsCount.innerText) || 0;
    requestsCount.innerText = currentRequests - 1;

      // when click on accept increase the number of your connection
    if(this.classList.contains("true")){
      let currentConnections = parseInt(connectionsCount.innerText) || 0;
      connectionsCount.innerText = currentConnections + 1;
    }
  });
});
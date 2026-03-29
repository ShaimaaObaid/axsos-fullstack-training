//alert message
function selectCity() {
    alert("Loading weather report...");
}
//hide cookie
function acceptCookies() {
    document.querySelector(".cookieDiv").style.display = "none";
}
//convert the temprature
document.querySelector("#temp").addEventListener("change", convertTemp);

function convertTemp(e) {
    let temps = document.querySelectorAll(".high, .low");

    for (let i = 0; i < temps.length; i++) {
        let value = parseInt(temps[i].innerText);

        if (e.target.value === "f") {
            temps[i].innerText = Math.round(value * 9 / 5 + 32);
        } else {
            temps[i].innerText = Math.round((value - 32) * 5 / 9);
        }
    }
}
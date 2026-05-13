const newH1=document.createElement("h1")
const box1=document.getElementById("box1")
newH1.innerText="this is my first heading"
box1.append(newH1)
const mybutton=document.getElementById("mybutton")
mybutton.addEventListener("click",function(mybutton){
const sec1=document.getElementById("section1")
const newDiv=document.createElement("div")
newDiv.id="box5"
newDiv.className="box"
const newP=document.createElement("p")
newP.innerText="Box5"
newDiv.append(newP)
sec1.append(newDiv)

})

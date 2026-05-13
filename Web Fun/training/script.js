function happyBirthday(username){
    console.log( "happy birthday to",username )
}
happyBirthday("khalid")
function add(x,y){
    let result=x+y
    return result
}
let answer=add(2,3)
console.log(answer)

function subtract(a,b){
    return a-b
}
console.log(subtract(2,3))

function isOdd(number){
    if(number%2===0){
        console.log(' number is even')
    }
    else{
        console.log("number is odd")
    }
}
isOdd(3)
function isEven(number){
    if(number%2===0){
        return true
    }
    else{
        return false
    }
}
console.log(isEven(12))




console.log("-----------")
const body=document.body
const div=document.querySelector('div')
const sapnHi=document.querySelector("#hii")
sapnHi.style.color="red"

const mybox=document.getElementById("myBox")
const mybutton=document.getElementById("myButton")
mybutton.addEventListener("click",function(event){
     mybox.style.backgroundColor="red"
     mybox.innerText="ouh"
})
//=>arrow fun
mybutton.addEventListener( "mouseover",event=>{
    event.target.style.backgroundColor="red"
     event.target.innerText="ouh"
})
mybutton.addEventListener( "mouseout",event=>{
    event.target.style.backgroundColor="lightblue"
     event.target.innerText="click me"
})
const myHeading=document.getElementById("my_heading")
myHeading.style.backgroundColor="yellow"
myHeading.style.textAlign="center"
//console.log(myHeading)

const fruits=document.getElementsByClassName("fruits")
//fruits[0].style.backgroundColor="yellow"
for(let fruit of fruits){
    fruit.style.backgroundColor="red"

}
const vegetables=document.getElementsByClassName("vegetables")
Array.from(vegetables).forEach(vegetable =>{
    vegetable.style.color="green"
})
const h4Elements=document.getElementsByTagName("h4")
//console.log(h4Elements)
//h4Elements[0].style.backgroundColor="blue"
//way1 for loop
for(let h4Element of h4Elements){
    h4Element.style.backgroundColor="black"
    h4Element.style.color="white"
}
//way2 for each
Array.from(h4Elements).forEach(h4Element=>{
    h4Element.style.backgroundColor="black"
    h4Element.style.color="white"
}
)
const elem=document.querySelector("h4")
elem.style.backgroundColor="blue"

const liElements=document.getElementsByTagName("li")
for (let liElement of liElements){
    liElement.style.backgroundColor="lightgreen"
}
Array.from(liElements).forEach(liElement=>{
    liElement.style.backgroundColor="lightgreen"
})

const allFruites=document.querySelectorAll(".fruits")
//allFruites[0].style.backgroundColor="gray"
allFruites.forEach(fruit =>{
    fruit.style.backgroundColor="gray"
})
const newH1=document.createElement("h1")
newH1.innerText="i like pizza"
newH1.id="myH1"
newH1.style.color="red"
newH1.style.textAlign="center"
//append element at the end of the body
document.body.append(newH1)
//append element at the start of the body
//document.body.prepend(newH1)
document.getElementById("box1").append(newH1)

const newP=document.createElement("p")
newP.innerText="this is my paragraph"
newP.style.color="green"
newP.id="myp"
document.getElementById("box2").append(newP)

//paragraph will appear before box2
const new2p=document.createElement("p")
new2p.innerText="this is my new paragraph will appear before box2"
const box2=document.getElementById("box2")
//document.body.insertBefore(new2p,box2)
//if the div did not have an id 
const boxes=document.querySelectorAll(".box")
document.body.insertBefore(new2p,boxes[0])
//remove html element
//document.body.removeChild(new2p)
//document.getElementById("box2").removeChild(newP)

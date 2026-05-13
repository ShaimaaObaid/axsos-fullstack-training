let hero_button=document.querySelector("#hero-button")
let button_p=document.querySelector("#button-p")
/*if u mean the text it self */
button_p.addEventListener("click",function(){
    hero_button.style.display="none"

})
/*if u mean the button it self */
hero_button.addEventListener("click",function(){
    hero_button.style.display="none"

})
/*change the img*/
let image = document.querySelector("#hero-img")
image.addEventListener("click",function(){
    image.src="static/blue-super-car.png"
})


let buttons=document.querySelectorAll(".col-div button")
buttons.forEach(btn=>{
    btn.onclick=function(){
        let div = btn.closest(".col-div")
        let p= div.querySelector(".booking")
        let num=parseInt(p.innerText)
        num--
        p.innerText=num +"Appointment Available"
    }
})




/*change img and text*/
let btn=document.getElementById("btn")
let img=document.getElementById("myImage")
let text=document.getElementById("text")
btn.addEventListener("click",function(){
    img.src="static/client.png"
    text.innerText="I had a great experience at the car wash .The service was quick and efficient,and my car was cleaned thoroughly with attention to detail .The staff were professional and committed to providing the best service possible .Additionally the prices were  reasonable considering the quality of the work .I will come definitely be coming back and would recommended this car wash to anyone looking for excellent service "

}) 




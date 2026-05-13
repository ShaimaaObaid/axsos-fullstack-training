const button = document.querySelector(".hero_button")
button.addEventListener("mouseover",function(){
    button.style.backgroundColor="#3b4598"
})
button.addEventListener("mouseout",function(){
    button.style.backgroundColor=""
})


const changeButton =document.querySelector(".about-button")
const changeImg =document.querySelector(".about_img")
const changeH3 =document.querySelector(".aboutH3")
const changeP =document.querySelector(".aboutP")
let isChanged = false
changeButton.addEventListener("click",function(){
   if(!isChanged){
     changeButton.innerText="Change Back"
     changeButton.className="about-button"
    changeImg.src="static/alt-features.png"
    changeH3.innerText="what we do"
    changeP.innerText="At our company,innovation drives everything we do .We specialize inleveaging cutting-edge technologies and strategic  expertise to empower businesses to grow smarter and faster .From enhancing digital experiences and optimizing internal workflows to unlocking new revenue opportunities"


    isChanged =true
   }
   else{
    changeButton.innerText="Make A Change"
    changeImg.src="static/about.jpg"
    changeH3.innerText="Who we are"
    changeP.innerText="We are a forward-thinking company dedicated to providing innovative solutions that fuel business growth. With a focus on modern technologies and strategic insights. we help businesses streamline their operations ,enhance customer experiences, and scale efficiently .Whether you're looking to improve your digital presence ,optimize processes, or drive new revenue streams ."

    isChanged =false
   }
    

})


const addButton=document.querySelector(".add-service")
const section=document.querySelector(".three_services_sec")
addButton.addEventListener("click",function(){
const newDiv=document.createElement("div")
newDiv.className="service"

const newImg=document.createElement("img")
newImg.src="static/features.png"
newImg.className="imgService"

const newP=document.createElement("p")
newP.innerText="Lorem ipsum dolor sit amet consectetur adipisicing elit. Aspernatur labore ea quae, assumenda quasi deserunt deleniti provident quod perferendis dolore. Accusamus dolorem aliquam sint ut cupiditate in ducimus facere dolore!"
section.append(newDiv)
newDiv.append(newImg)
newDiv.append(newP)
})




/*const addButton=document.querySelector(".add-service")
const section=document.querySelector(".three_services_sec")
addButton.addEventListener("click",function(){

let newDiv = document.createElement("div");
newDiv.className = "service";

newDiv.innerHTML = `
  <img src="img2.jpg" class="imgService">
  <p>Text 2</p>
`;

sec.appendChild(newDiv);
})*/
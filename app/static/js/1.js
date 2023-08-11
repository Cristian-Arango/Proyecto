setTimeout(function(){
    elementoP = document.querySelector('.msg');
    elementoP.style.display = 'none';
}, 2000);

//Nombre 
const form=document.getElementById("formulariodelcliente")

//acceder al ficback
resulte=document.querySelector("#nombreCliente .feedback")

let flag2
form.nombre.addEventListener('input',(e)=>{
    e.preventDefault()
    alert("Se esta escriendo sobre el input")
    if(text.test(e.target.value)){
        form.nombre.setAttribute("class","success")
        resulte.style.setProperty("visibility","hidden")
        resulte.style.setProperty("opacity","0")
        flag2=true
    
    
    }
    else{
        form.nombre.setAttribute("class","error")
        resulte.textContent="Por favor digite bien su nombre "
        resulte.style.setProperty("visibility","visible")
        resulte.style.setProperty("opacity","1")
        flag2=false
        
    }
    })
    
    
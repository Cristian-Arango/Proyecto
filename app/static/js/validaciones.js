const form=document.getElementById("formulariodelcliente")
const nom=form.nombreCliente.value
alert("Helou world")

form.nom.addEventListener('input',(e)=>{
    e.preventDefault()
    alert("Se esta escriendo sobre el input")
  
    
    
    })
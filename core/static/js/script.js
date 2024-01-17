const $btnsEliminar = document.querySelectorAll("#btn-eliminar")
const $formulario = document.querySelector("#formulario")
const $inputTarea = document.querySelector("#input-tarea")

$formulario.addEventListener("submit", function(e){
    let nombre = String($inputTarea.value).trim()
    if (nombre.length === 0){
        e.preventDefault()
        Swal.fire({
            titleText: "Precaución",
            text: "No debe ingresar espacios en blanco",
            icon: "error",
            confirmButtonObject: "Ok!",
        })
    }
})

$btnsEliminar.forEach((btn, index) =>{
    btn.addEventListener("click", function(e){
        let $nombreTarea = document.querySelectorAll("#tarea")
        e.preventDefault()
        Swal.fire({
            title: `¿Está seguro que desea eliminar la tarea\n "${$nombreTarea[index].textContent}"?`,
            showCancelButton: true,
            confirmButtonText: "Eliminar",
            confirmButtonColor: "crimson",
            backdrop: true,
            showLoaderOnConfirm: true,
            preConfirm: ()=>{
                location.href = e.target.href
            },
            allowOutsideClick: ()=>false,
            allowEscapeKey: ()=>false
        })

    } )

})

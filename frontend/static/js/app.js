/* Previene la acción por defecto del formulario (enviar contenido como parametro de url) */
let form = document.querySelector(".form")
form.addEventListener("submit", function(event){
    event.preventDefault();
});

let input = document.querySelector(".input");
let msj_datos = document.getElementById("message");
let boton = document.getElementById("button-send");

function getData() {
    console.log("Boton presionado");
    msj_datos.style.display = "none";

    msj_datos.innerHTML = '';
   
    data = input.value;

    console.log("Enviado: " + data);

    axios.get(`http://192.168.0.138:5008/api/${data}`)
    .then(function (response) {
        console.log(response.data); //Me muestra la parte de datos del paquete HTTP que devuelve el GET

        msj_datos.style.display = "block";

        msj_datos.innerHTML = `<div>
                                    <strong>Recibido desde el backend: ${response.data.dato_enviado}</strong>
                                </div>`;
    })
    .catch(function (error) {

        console.log('Error');

        msj_datos.style.display = "block";

        msj_datos.innerHTML = `<div>
                                    <strong>Error</strong>
                                </div>`;

    });
       
        
}

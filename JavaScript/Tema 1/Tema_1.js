function Calcular_Propina() {

    let output = document.getElementById('Output');
// Calcular la propina y el total a pagar
var propina = montoBoleta * (porcentajePropina / 100);
var totalPagar = parseFloat(dinero) + propina;

var resultadoElement = document.getElementById("resultado");
    resultadoElement.innerHTML = "Monto de la propina: " + propina + " CLP<br>";
    resultadoElement.innerHTML += "Total a pagar (incluyendo propina): " + totalPagar + " CLP";

}

document.getElementById('Boton_Calcular').addEventListener('click',Calcular_Propina); // Trae el elemento del html 'Boton_Calcular' y que debe estar atento a lo que pase con boton,
                                                                                    //  cuando hagan click, debe ejecutar 'Calcular_Propina'

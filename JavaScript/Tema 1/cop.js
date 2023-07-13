function Calcular_Propina() {
    // Obtener el valor del monto de la boleta y el porcentaje de propina seleccionado
    let total_Boleta = document.getElementById("boleta").value;
    let ptje_Propina = document.getElementById("porcentaje").value;

    // Validar que se haya ingresado un número válido como monto de la boleta
    if (isNaN(total_Boleta), total_Boleta <= 0) {
        alert("ERROR, ingrese un monto de boleta que sea valido porfavor");
        return;
    }

    // Calcular la propina y el total a pagar
    let propina = total_Boleta * (ptje_Propina / 100);
    let totalPagar = parseFloat(total_Boleta) + propina;

    // Mostrar el resultado en pantalla
    let resultado = document.getElementById("resultado");
    resultado.innerHTML = "Propina: $" + propina + " CLP <br>";
    resultado.innerHTML += "Total a pagar: $" + totalPagar + " CLP";
}
        
<?php
// Datos de conexión a la base de datos
$servername = "proyecto_integrador";
$username = "root";
$password = "";
$dbname = "registrar asistencia";

// Obtener los datos del formulario
$nombre = $_POST['nombre'];
$rut = $_POST['run'];
$asignatura = $_POST['asignatura'];
$añoingreso = $_POST['año ingreso'];
$sede = $_POST['sede']

// Crear la conexión a la base de dato

$conn = new mysqli($servername, $username, $password, $dbname);

// Verificar la conexión
if ($conn->connect_error) {
    die("Error en la conexión a la base de datos: " . $conn->connect_error);
}

// Preparar y ejecutar la consulta SQL para insertar los datos en la tabla correspondiente
$sql = "INSERT INTO asistencia (nombre, rut, asignatura, añoingreso, sede) VALUES ('$nombre', '$rut', '$asignatura', '$añoingreso', '$sede')";

if ($conn->query($sql) === TRUE) {
    echo "La asistencia se ha registrado correctamente.";
} else {
    echo "Error al registrar la asistencia: " . $conn->error;
}

// Cerrar la conexión a la base de datos
$conn->close();
?>
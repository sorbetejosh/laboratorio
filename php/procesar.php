<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nombre = $_POST['nombre'];
    $direccion = $_POST['direccion'];
    $correo = $_POST['correo'];
    $genero = $_POST['genero'];
    
    echo "Hola, $nombre! Vives en $direccion y tu correo es $correo. Tu género es $genero.";
}
?>

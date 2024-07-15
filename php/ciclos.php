<?php
// configurar un cookie
setcookie("usuario","juan", time() + (86400*30),"/"); //86400 = 1 dia
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Cookie  Test</title>
    <title>Ciclo for en PHP</title>
</head>
<body>
    <h1>Cookie Set</h1>
    <?php
    //verificar si la cookie esta configurada 
    if(isset($_COOKIE["usuario"])){
        echo "Cookie 'usuario' esta configurada. Valor:".
$_COOKIE ["usuario"];
    } else{        
        echo "Cookie 'usuario' no esta configurada.";
    }
    ?>
    <h1>Ciclo for</h1>
    <u1>
        <?php
        for ($i = 1; $i <= 5; $i++) {
            echo "<li>Elemento $i</1li>";
        }    
        ?>
    </u1>
</body>
</html>        
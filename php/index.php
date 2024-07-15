<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulario con imagen de fondo</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-image: url('"C:\Users\ej.cuellar\Pictures\Screenshots\Captura de pantalla 2024-07-10 135523.png"'); /* Ruta a tu imagen de fondo */
            background-size: cover; /* Ajusta la imagen al tamaño del contenedor */
            background-position: center; /* Centra la imagen */
            padding: 20px;
        }
        .formulario {
            max-width: 400px;
            margin: 0 auto;
            background-color: rgba(255, 255, 255, 0.8); /* Fondo blanco semitransparente */
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            color: #333333;
        }
        label {
            display: block;
            margin-bottom: 10px;
            color: #666666;
        }
        input[type="text"],
        input[type="email"],
        input[type="radio"] {
            width: calc(100% - 22px); /* ajuste para el borde */
            padding: 10px;
            border: 1px solid #cccccc;
            border-radius: 4px;
            font-size: 16px;
        }
        input[type="submit"] {
            width: 100%;
            padding: 10px;
            border: none;
            background-color: #007bff;
            color: #ffffff;
            font-size: 16px;
            cursor: pointer;
            border-radius: 4px;
        }
        input[type="submit"]:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="formulario">
        <h1>Bienvenido al formulario</h1>
        <form action="procesar.php" method="post">
            <label for="nombre">Nombre:</label>
            <input type="text" id="nombre" name="nombre" required><br><br>
            
            <label for="direccion">Dirección:</label>
            <input type="text" id="direccion" name="direccion" required><br><br>
            
            <label for="correo">Correo electrónico:</label>
            <input type="email" id="correo" name="correo" required><br><br>
            
            <label>Género:</label>
            <input type="radio" id="masculino" name="genero" value="Masculino" required>
            <label for="masculino">Masculino</label>
            
            <input type="radio" id="femenino" name="genero" value="Femenino">
            <label for="femenino">Femenino</label><br><br>
            
            <input type="submit" value="Enviar">
        </form>
    </div>
</body>
</html>

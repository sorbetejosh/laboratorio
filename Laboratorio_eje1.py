#Crear un programa que permita convertir temperaturas entre Celsius y Fahrenheit. El programa debe proporcionar un menú interactivo para que el usuario elija la conversión deseada.

print("eliga la opcion que quiere opcion 1 celcius a fahrenheit opcion 2 fahrenheit a celcius 3 salir del programa")
ingreselaopcion=int(input("introduzca entre 1, 2 o 3"))

opcion1=("celcius a fahrenheit")
opcion2=("fahrenheit a celcius")

if ingreselaopcion ==1:
    celcius=float(input("ingrese los grados a convertir a celcius "))
    operacion1=((celcius*9/5)+32)
    print(operacion1,"celcius")

elif ingreselaopcion ==2:
    fahrenheit=float(input("ingrese los grados a convertir a fahrenheit "))
    operacion2=((fahrenheit-32)*5/9)
    print(operacion2,"fahrenheit")

elif ingreselaopcion ==3:
    print("saliendo del programa")


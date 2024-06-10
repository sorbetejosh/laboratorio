#Crear un programa que gestione el inventario de una tienda. 
#El programa permitirá al usuario realizar diferentes operaciones en la matriz de inventario,
#cómo agregar productos, eliminar productos, actualizar cantidades, y consultar el inventario.
# Cada producto tendrá un nombre, una cantidad y un precio.

print("RELGAS DE LA TIENDA")
print("AL MOMENTO DE AGREGAR PRODUCTOS SEPARARLOS POR COMAS")
print("AL ELIMINAR PRODUCTOS EL NUMERO INICIAL ES 0 ")
print("eliga la opcion que quiere realizar en la tienda")
print("opcion (1): agregar productos")
print("opcion (2): eliminar productos")
print("opcion (3): actualizar la cantidad de un producto")
print("opcion (4): consultar el inventario completo")
print("opcion (5):salir de el programa")
intento=int(input("ingrese la opcion que quiere realizar "))
lista=[]
valor3=['fresa'  ,'sandia'   ,'pera'  ,' melon'  ,' papaya'   ,'pepino'    ,'lechuga'     ,'consome'     ,'pan ']
valor=['fresa 100'  ,'sandia 200'   ,'pera 50'  ,' melon 900'  ,' papaya 500'   ,'pepino 20'    ,'lechuga 10'     ,'consome 67'     ,'pan 87']

valor1=['100'  ,'200'   ,'50'  ,'900'  ,'500'   ,'20'    ,'10'     ,'67'     ,'87']
print("ESTAS SON LAS OPCIONES Y PRECIOS")
print (valor3)
print(valor1)

if intento == 1:
    print("que quiere agregar")
    opcion1=str(input("ingrese lo que quiere agregar "))
    lista.append(opcion1)
    print(lista)

elif intento ==2:
    print("que quiere eliminar")
    opcion2=int(input("ingrese lo que quiere eliminar "))
    lista.pop(opcion2)
    print(lista)

elif intento ==3:
    print("cantidad a actualizar")
    opcion3=int(input("ingrese el producto a actualizar"))
    precio=int(input("ingrese precio nuevo "))
    valor1[opcion3]=(precio)
    print(valor1)

elif intento ==4:
    print(lista)


elif intento ==5:
    print("saliendo del programa, gracias por estar en la tienda")



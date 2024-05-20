import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Conectar a la base de datos
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="colegio"
)
mycursor = mydb.cursor()

# Verificar si la tabla existe, si no, crearla
mycursor.execute('''CREATE TABLE IF NOT EXISTS estudiantes (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(255) NOT NULL,
                    identificacion VARCHAR(255) NOT NULL,
                    asistencia VARCHAR(255) NOT NULL
                )''')

def agregar_estudiante():
    nombre = entry_nombre.get().strip()
    identificacion = entry_identificacion.get().strip()
    asistencia = asistencia_var.get()

    if nombre != '' and identificacion != '':
        # Insertar el estudiante en la base de datos
        sql = "INSERT INTO estudiantes (nombre, identificacion, asistencia) VALUES (%s, %s, %s)"
        val = (nombre, identificacion, asistencia)
        mycursor.execute(sql, val)
        mydb.commit()
        
        # Actualizar la lista en la interfaz gráfica
        item = f"Nombre: {nombre}, Identificación: {identificacion}, Asistencia: {asistencia}"
        lista_estudiantes.insert(tk.END, item)
        entry_nombre.delete(0, tk.END)
        entry_identificacion.delete(0, tk.END)
        asistencia_var.set("Presente")
    else:
        messagebox.showwarning(
            "Error", "Debes ingresar el nombre y la identificación del estudiante.")

def eliminar_estudiante():
    seleccionado = lista_estudiantes.curselection()
    if seleccionado:
        # Obtener la información del estudiante seleccionado
        item = lista_estudiantes.get(seleccionado)
        identificacion = item.split(", ")[1].split(": ")[1]
        
        # Eliminar el estudiante de la base de datos
        sql = "DELETE FROM estudiantes WHERE identificacion = %s"
        val = (identificacion,)
        mycursor.execute(sql, val)
        mydb.commit()
        
        # Eliminar el estudiante de la lista en la interfaz gráfica
        lista_estudiantes.delete(seleccionado)
        entry_nombre.delete(0, tk.END)
        entry_identificacion.delete(0, tk.END)
        asistencia_var.set("Presente")
    else:
        messagebox.showwarning(
            "Error", "Debes seleccionar un estudiante para eliminar.")

def actualizar_estudiante():
    nombre = entry_nombre.get().strip()
    identificacion = entry_identificacion.get().strip()
    asistencia = asistencia_var.get()

    if nombre != '' and identificacion != '':
        nuevo_item = f"Nombre: {nombre}, Identificación: {identificacion}, Asistencia: {asistencia}"
        seleccionado = lista_estudiantes.curselection()

        if seleccionado:
            # Obtener la información del estudiante seleccionado
            item = lista_estudiantes.get(seleccionado)
            vieja_identificacion = item.split(", ")[1].split(": ")[1]
            
            # Actualizar el estudiante en la base de datos
            sql = "UPDATE estudiantes SET nombre = %s, asistencia = %s WHERE identificacion = %s"
            val = (nombre, asistencia, vieja_identificacion)
            mycursor.execute(sql, val)
            mydb.commit()
            
            # Actualizar la lista en la interfaz gráfica
            lista_estudiantes.delete(seleccionado)
            lista_estudiantes.insert(seleccionado, nuevo_item)
        else:
            messagebox.showwarning(
                "Error", "Debes seleccionar un estudiante para actualizar.")
    else:
        messagebox.showwarning(
            "Error", "Debes ingresar el nombre y la identificación del estudiante.")

ventana = tk.Tk()
ventana.title("Gestión de Estudiantes")

frame_datos = tk.Frame(ventana)
frame_datos.pack()

label_nombre = tk.Label(frame_datos, text="Nombre:")
label_nombre.grid(row=0, column=0)
entry_nombre = tk.Entry(frame_datos)
entry_nombre.grid(row=0, column=1)

label_identificacion = tk.Label(frame_datos, text="Identificación:")
label_identificacion.grid(row=1, column=0)
entry_identificacion = tk.Entry(frame_datos)
entry_identificacion.grid(row=1, column=1)

frame_asistencia = tk.Frame(ventana)
frame_asistencia.pack()

asistencia_var = tk.StringVar(value="Presente")

label_asistencia = tk.Label(frame_asistencia, text="Asistencia:")
label_asistencia.pack()

radio_presente = tk.Radiobutton(
    frame_asistencia, text="Presente", variable=asistencia_var, value="Presente")
radio_presente.pack()

radio_ausente = tk.Radiobutton(
    frame_asistencia, text="Ausente", variable=asistencia_var, value="Ausente")
radio_ausente.pack()

frame_botones = tk.Frame(ventana)
frame_botones.pack()

boton_agregar = tk.Button(
    frame_botones, text="Agregar", command=agregar_estudiante)
boton_agregar.pack(side=tk.LEFT)

boton_eliminar = tk.Button(
    frame_botones, text="Eliminar", command=eliminar_estudiante)
boton_eliminar.pack(side=tk.LEFT)

boton_actualizar = tk.Button(
    frame_botones, text="Actualizar", command=actualizar_estudiante)
boton_actualizar.pack(side=tk.LEFT)

frame_lista = tk.Frame(ventana)
frame_lista.pack()

lista_estudiantes = tk.Listbox(frame_lista, width=50, height=10)
lista_estudiantes.pack()

ventana.mainloop()

# Cerrar la conexión con la base de datos
mycursor.close()
mydb.close()

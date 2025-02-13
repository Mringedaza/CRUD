
import tkinter as tk 

from tkinter import *

from tkinter import ttk
from tkinter import messagebox

from Clientes import *
from Conexion import *

# Creacion para el formulario   
class formularioClientes: 

    global base 
    base = None

    global texBoxId
    texBoxId = None

    global texBoxNombre
    texBoxNombre = None

    global texBoxApellido
    texBoxApellido = None

    global combo
    combo = None

    global texBoxEdad
    texBoxEdad = None

    global groupBox
    groupBox = None

    global tree
    tree  = None


def formulario():

        global base 
        global texBoxId
        global texBoxNombre
        global texBoxApellido
        global texBoxEdad
        global combo
        global groupBox
        global tree

        try:
            base = Tk()
            base.geometry("1800x500")
            base.title("Formulario")

            groupBox = LabelFrame(base, text="Datos personales", padx=5, pady=5)
            groupBox.grid(row=0, column=0, padx=10,pady=10)

            LabelCedula=Label(groupBox,text="Cedula:", width=13, font=("arial", 12)).grid(row=0,column=0)
            texBoxId = Entry(groupBox)
            texBoxId.grid(row=0, column=1)

            LabelNombre=Label(groupBox,text="Nombre:", width=13, font=("arial", 12)).grid(row=1,column=0)
            texBoxNombre = Entry(groupBox)
            texBoxNombre.grid(row=1, column=1)

            LabelApellido=Label(groupBox,text="Apellido:", width=13, font=("arial", 12)).grid(row=2,column=0)
            texBoxApellido = Entry(groupBox)
            texBoxApellido.grid(row=2, column=1)

            LabelEdad=Label(groupBox,text="Edad:", width=13, font=("arial", 12)).grid(row=3,column=0)
            texBoxEdad = Entry(groupBox)
            texBoxEdad.grid(row=3, column=1)

            Labelsexo=Label(groupBox,text="Sexo:", width=13, font=("arial", 12)).grid(row=4,column=0)
            seleccionSexo=tk.StringVar()
            combo=ttk.Combobox(groupBox,values=["Masculino","Femenino"], textvariable=seleccionSexo)
            combo.grid(row=4,column=1)
            seleccionSexo.set("Masculino")

            Button(groupBox, text="Guardar", width=10, command=guardarRegistros).grid(row=5,column=0)
            Button(groupBox, text="Modificar", width=10, command=modificarRegistros).grid(row=5,column=1)
            Button(groupBox, text="Eliminar", width=10, command=EliminarRegistros).grid(row=5,column=2)

            groupBox = LabelFrame(base,text="Personas Registradas", padx=5, pady=5,)
            groupBox.grid(row=0,column=1,padx=5,pady=5)


        #configuracion de columnas con treeview 

            tree = ttk.Treeview(groupBox,columns=("Cedula", "Nombre", "Apellido", "Edad","Sexo",),show='headings',height=5,)
            tree.column("# 1",anchor=CENTER)
            tree.heading("# 1", text="Cedula",)

            tree.column("# 2",anchor=CENTER)
            tree.heading("# 2", text="Nombre",)

            tree.column("# 3",anchor=CENTER)
            tree.heading("# 3", text="Apellido",)

            tree.column("# 4",anchor=CENTER)
            tree.heading("# 4", text="Edad",)

            tree.column("# 5",anchor=CENTER)
            tree.heading("# 5", text="Sexo",)

            for row in CClientes.MostrarClientes():
                 tree.insert("","end",values=row)

            tree.bind("<<TreeviewSelect>>",selecionarRegistro)

            tree.pack()
            
            base.mainloop()




        except ValueError as error:
            print("Error al mostrar la interfaz, error: {}" .format(error))

def guardarRegistros():
        
        global texBoxId, texBoxNombre, texBoxApellido, texBoxEdad, combo, groupBox


        try: 

            if texBoxId is None or texBoxNombre is None or texBoxApellido is None or texBoxEdad is None or combo is None:
                print("Botones no inicializados") 
                return
            cedula = texBoxId.get()
            nombres = texBoxNombre.get()
            apellidos = texBoxApellido.get() 
            edad = texBoxEdad.get()
            sexo = combo.get()

            if not cedula or not nombres or not apellidos or not edad:
                messagebox.showinfo("Informacion","Comeplete los datos")
            else:
                CClientes.IngresoDeClientes(cedula, nombres, apellidos, edad, sexo)
                messagebox.showinfo("Informacion","Los datos fueron agregados correctamente")

            actualizarTreeview()

            texBoxId.delete(0,END)
            texBoxNombre.delete(0,END)
            texBoxApellido.delete(0,END)
            texBoxEdad.delete(0,END)
        except ValueError as error:
            print("Error al ingresar datos {}".format(error))

def actualizarTreeview():
    global tree

    try:
        tree.delete(*tree.get_children())

        datos = CClientes.MostrarClientes()

        for row in CClientes.MostrarClientes():
            tree.insert("","end",values=row)

    except ValueError as error:
         print("Error al actualizar tabla {}". format(error))
        
def selecionarRegistro(event):
     try:
        registroSeleccionado =  tree.focus()

        if registroSeleccionado:
             values = tree.item(registroSeleccionado)['values']

             texBoxId.delete(0,END)
             texBoxId.insert(0,values[0])

             texBoxNombre.delete(0,END)
             texBoxNombre.insert(0,values[1])

             texBoxApellido.delete(0,END)
             texBoxApellido.insert(0,values[2])

             texBoxEdad.delete(0,END)
             texBoxEdad.insert(0,values[3])

             combo.set(values[4])

     except ValueError as error:
        print("Error al seleccionar registro {}".format(error))


def modificarRegistros():
        
        global texBoxId, texBoxNombre, texBoxApellido, texBoxEdad, combo, groupBox


        try: 

            if texBoxId is None or texBoxNombre is None or texBoxApellido is None or texBoxEdad is None or combo is None:
                print("Botones no inicializados") 
                return
            cedula = texBoxId.get()
            nombres = texBoxNombre.get()
            apellidos = texBoxApellido.get() 
            edad = texBoxEdad.get()
            sexo = combo.get()

            if not cedula or not nombres or not apellidos or not edad:
                messagebox.showinfo("Informacion","Los datos no pueden estar vacios")
            else:
                CClientes.modificarClientes(cedula, nombres, apellidos, edad, sexo)
                messagebox.showinfo("Informacion","Los datos fueron actualizados correctamente")

            actualizarTreeview()

            texBoxId.delete(0,END)
            texBoxNombre.delete(0,END)
            texBoxApellido.delete(0,END)
            texBoxEdad.delete(0,END)
        except ValueError as error:
            print("Error al actualizar datos {}".format(error))

def EliminarRegistros():
        
        global texBoxId, texBoxNombre, texBoxApellido, texBoxEdad


        try: 

            if texBoxId is None:
                print("Botones no inicializados") 
                return
            cedula = texBoxId.get()
    
            if not cedula:
                messagebox.showinfo("Informacion","No hay datos para eliminar")
            
            else:
                CClientes.EliminarClientes(cedula)
                messagebox.showinfo("Informacion","Los datos fueron eliminados correctamente")

            actualizarTreeview()

            texBoxId.delete(0,END)
            texBoxNombre.delete(0,END)
            texBoxApellido.delete(0,END)
            texBoxEdad.delete(0,END)
        except ValueError as error:
            print("Error al eliminar los datos {}".format(error))

formulario()
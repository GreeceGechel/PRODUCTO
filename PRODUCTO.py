from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import messagebox, ttk





root=Tk()
root.geometry("300x500")

ventanaPrin=Frame(root)
ventanaPrin.grid(row=1,column=1)

titulo0=Label(ventanaPrin,text="Registro\nproductos",font=("Roboto",20))
titulo0.grid(row=5,column=3,padx=5,pady=5)

titulo=Label(ventanaPrin,text="Producto:",font=("Roboto",10))
titulo.grid(row=11,column=2,padx=5,pady=5)

titulo2=Label(ventanaPrin,text="Sku:",font=("Roboto",10))
titulo2.grid(row=12,column=2,padx=5,pady=5)

titulo3=Label(ventanaPrin,text="Height",font=("Roboto",10))
titulo3.grid(row=13,column=2,padx=5,pady=5)

control=IntVar()
preserve=Checkbutton(ventanaPrin, text="A",variable=control,font=("Roboto",10))
preserve.grid(row=15,column=2,pady=1)

control2=IntVar()
preserve=Checkbutton(ventanaPrin, text="B",variable=control2,font=("Roboto",10))
preserve.grid(row=15,column=3,pady=1)

control3=IntVar()
preserve=Checkbutton(ventanaPrin, text="C",variable=control3,font=("Roboto",10))
preserve.grid(row=15,column=4,pady=1)


textoNombre=Entry(ventanaPrin,font=("Roboto",10)).grid(row=11,column=3,padx=5,pady=5)
textoheig=Entry(ventanaPrin,font=("Roboto",10)).grid(row=12,column=3,padx=5,pady=5)

imgBart = Image.open('C:\\Users\\Junio\\OneDrive\\Escritorio\\PROGRAMAS DE PYTHON\\INTERFAZ_GRAFICA\\telmex.png')

#Variable que contiene el nombre de la imagen

imagenMusica = imgBart.resize((90,80))

imag = ImageTk.PhotoImage(imagenMusica)
miTitulo = Label(ventanaPrin,image=imag)
miTitulo.grid(row=6,column=3,padx=5,pady=5)

proveedor=Label(ventanaPrin,text="Proveedor:",font=("Roboto",10))
proveedor.grid(row=20,column=2,padx=5,pady=5)


lista=tk.Listbox(ventanaPrin,selectmode=(),width=10,height=1)

lista.insert(END, "TELMEX","Megacable","Cable")
list=tk.Scrollbar(ventanaPrin,orient=tk.VERTICAL)
lista.grid(row=20,column=3)

lista_desplegable=ttk.Combobox(ventanaPrin,width=17)
lista_desplegable.grid(row=20,column=3)
opciones=["CABLE","TELMEX","MEGACABLE"]
lista_desplegable['values']=opciones



Idioma=Label(ventanaPrin,text="Idioma:",font=("Roboto",10))
Idioma.grid(row=24,column=2,padx=5,pady=5)

idioma1=IntVar()
preserve=Checkbutton(ventanaPrin, text="EN",variable=idioma1,font=("Roboto",10))
preserve.grid(row=25,column=3,pady=1)

idioma2=IntVar()
preserve=Checkbutton(ventanaPrin, text="SP",variable=idioma2,font=("Roboto",10))
preserve.grid(row=25,column=4,pady=1)

Registrar=Button(ventanaPrin,text="Registrar", bg="#008000",fg="#FFFACD",font=("Roboto",15,"bold"),width=10,height=1)
Registrar.grid(row=30,column=3,pady=1)

root.mainloop()
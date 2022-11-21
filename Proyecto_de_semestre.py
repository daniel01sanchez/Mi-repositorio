import tkinter
from tkinter.font import Font

ventana = tkinter.Tk()
ventana.geometry("1000x640")

etiqueta = tkinter.Label(ventana, text = "Aprende a Programar Python Básico", bg = "steelblue", font = "Verdana 13")
etiqueta.pack(fill = tkinter.BOTH, expand = True)

img = tkinter.PhotoImage(file="pythoniloghio.png")
ibl_img = tkinter.Label(ventana, image = img, bg = "lightsteelblue")
ibl_img.pack(fill = tkinter.X, expand = True)

etiqueta_2 = tkinter.Label(ventana, text = "¿Qué quieres aprender hoy?", bg = "steelblue", font = "Helvetica")
etiqueta_2.pack(fill = tkinter.X, expand = True)

boton_1 = tkinter.Button(ventana, text = "Tipos de Datos")
boton_1.pack(side = tkinter.BOTTOM)

boton_2 = tkinter.Button(ventana, text = "Comparaciones")
boton_2.pack(side = tkinter.BOTTOM)

boton_3 = tkinter.Button(ventana, text = "Condicionales")
boton_3.pack(side = tkinter.BOTTOM)

boton_4 = tkinter.Button(ventana, text = "Ciclos")
boton_4.pack(side = tkinter.BOTTOM)
ventana.mainloop()

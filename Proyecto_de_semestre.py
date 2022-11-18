import tkinter
from tkinter.font import Font

ventana = tkinter.Tk()
ventana.geometry("1000x580")

etiqueta = tkinter.Label(ventana, text = "Aprende a Programar Python Básico", bg = "steelblue", )
etiqueta.pack(fill = tkinter.BOTH, expand = True)

img = tkinter.PhotoImage(file="pythoniloghio.png")
ibl_img = tkinter.Label(ventana, image = img, bg = "lightsteelblue")
ibl_img.pack(fill = tkinter.X, expand = True)


boton_1 = tkinter.Button(ventana, text = "Inicia ahora")
boton_1.pack(side = tkinter.BOTTOM)

ventana.mainloop()


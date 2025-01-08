import tkinter as tk

app = tk.Tk() #ventana principal
###### Dimensionaes (altura por anchura)
app.geometry("300x600")
app.configure(background="black")

######Strings
##guardar strungs para widgets
palabra = tk.StringVar(app)
entrada = tk.StringVar(app)

#####para cambiar palabras
def cambiarPalabra():
    palabra.set("Suscribete " + entrada.get()) #actualiuzar valor


#título
tk.Wm.wm_title(app, "Mi primera GUI")


####### agregar widget
tk.Button(
    #Incrustar
    app,
    text="Click",
    font=("Times New Roman", 14),
    bg ="#00a8e8",
    fg="white",
    command= cambiarPalabra,
    relief = "sunken"
).pack( #este método nos permite colocar el button
    fill = tk.BOTH, #llenar alto y ancho
    expand=True
)

tk.Label(
    app,
    text="Etiqueta",
    textvariable=palabra,
    fg = "white",
    bg = "black",
    justify = "center"
).pack( #este método nos permite colocar el button
    fill = tk.BOTH, #llenar alto y ancho
    expand=True
)

tk.Entry(
    app,
    fg = "white",
    bg = "black",
    justify = "center",
    textvariable=entrada
).pack( #este método nos permite colocar el button
    fill = tk.BOTH, #llenar alto y ancho
    expand=True
)



app.mainloop() #refrescando la app, lo q se ve en pantalla



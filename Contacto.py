import tkinter as tk

# Crear una ventana
ventana = tk.Tk()
ventana.title("Información de Contacto")

# Maximizar la ventana automáticamente (modo de pantalla completa)
ventana.attributes('-fullscreen', False)

# Obtener el ancho y alto de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

# Cargar la imagen de fondo

# Configurar el tamaño y la posición de la ventana
ventana.geometry("{}x{}+0+0".format(ancho_pantalla, alto_pantalla))

# Crear un widget de etiqueta para mostrar la imagen de fondo



# Crear un widget de etiqueta para el texto
texto = tk.Label(ventana, text="ING. Andres Luna\nContacto: isdriw@gmail.com\nCell: 3128919009\n2023\nAF",
                 font=("century gothic", 24), fg="black")

# Configurar el texto para centrarlo vertical y horizontalmente
texto.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Iniciar el bucle de la interfaz gráfica
ventana.mainloop()



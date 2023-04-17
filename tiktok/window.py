import tkinter as tk
from tkinter import Label, Entry, Text, Button
from tkinter import DISABLED, NORMAL
from main import browser


def create_users(country):
    numero = entrada.get()
    try:
        numero = int(numero)
        print(country)
        #text box
        Label(text="").pack()
        btn1.config(state=DISABLED)
        text_box = Text(window,  height=10, width=50, padx=10, pady=10)
        info = f"Creating {numero} accounts in {country}\nWhen finish,I'll write to you by email and whatsapp\n..."
        text_box.insert(0.50,info) 
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 0.9, "end")
        text_box.pack()
        window.iconify()
        browser(numero, country)
    except ValueError:
        print("Error: Debe ingresar un número válido")

def validar(c):
    return c.isdigit()

window = tk.Tk()
window.geometry("290x370")
window.resizable(False, False)
window.title("{Sin nombre}")
Label(text="USERS",fg="#F4FEFF", bg="#2D61A6", width="40", height="2" ,font=("Arial 16")).pack()

Label(text="Select country").pack()


opcion_seleccionada = tk.StringVar()

opciones = ["USA", "MEXICO", "BRAZIL"]

menu = tk.OptionMenu(window, opcion_seleccionada, *opciones)
menu.pack()

def asignar_comando(*args):
    global region
    if opcion_seleccionada.get() == "USA":
        region = "en_US"
    elif opcion_seleccionada.get() == "MEXICO":
        region = "es_MX"

    elif opcion_seleccionada.get() == "BRAZIL":
        region = "pt_BR"


opcion_seleccionada.trace("w", asignar_comando)

validacion = window.register(validar)
Label(text="Users quantity").pack()

entrada = Entry(window, validate="key", validatecommand=(validacion, '%S'))
entrada.pack()
print(f"test: {opcion_seleccionada.get()}")
print(type(opcion_seleccionada.get()))


Label(text="").pack()

btn1 = Button(window,text="CREATE", state=NORMAL,height="3", width="10",bg="#9C9C9C", command=lambda:[create_users(region)])
btn1.pack()

window.mainloop()

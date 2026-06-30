"""
app.py
Interfaz gráfica con Tkinter para gestionar memorias USB:
- Mostrar dispositivos conectados
- Verificar
- Formatear
- Restaurar respaldos
"""

import tkinter as tk
from tkinter import ttk, messagebox
from backend import usb_manager   # aquí están listar, verificar, formatear
from backend import utils         # aquí están restaurar_respaldo, log_event

def mostrar_dispositivos():
    salida = usb_manager.listar_dispositivos()
    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, salida)

def verificar():
    device = entry_device.get()
    resultado = usb_manager.verificar_usb(device)
    messagebox.showinfo("Resultado", resultado)

def formatear():
    device = entry_device.get()
    resultado = usb_manager.formatear_usb(device)
    messagebox.showinfo("Resultado", resultado)

def restaurar():
    origen = "respaldo"  # carpeta de respaldo en la Pi
    destino = f"/media/{entry_device.get()}"
    resultado = utils.restaurar_respaldo(origen, destino)
    messagebox.showinfo("Resultado", resultado)

# Ventana principal
root = tk.Tk()
root.title("Gestor de USB")
root.geometry("800x600")

frame = ttk.Frame(root, padding=20)
frame.pack(fill="both", expand=True)

# Entrada de dispositivo
ttk.Label(frame, text="Dispositivo (ej. sda1):", font=("Arial", 14)).pack()
entry_device = ttk.Entry(frame, font=("Arial", 14))
entry_device.pack(pady=10)

# Botones grandes para pantalla táctil
ttk.Button(frame, text="Listar dispositivos", command=mostrar_dispositivos).pack(pady=15, ipadx=10, ipady=10)
ttk.Button(frame, text="Verificar USB", command=verificar).pack(pady=15, ipadx=10, ipady=10)
ttk.Button(frame, text="Formatear USB", command=formatear).pack(pady=15, ipadx=10, ipady=10)
ttk.Button(frame, text="Restaurar respaldo", command=restaurar).pack(pady=15, ipadx=10, ipady=10)

# Caja de texto para salida
text_box = tk.Text(frame, height=15, font=("Consolas", 12))
text_box.pack(fill="both", expand=True)

# Mantener ventana abierta
root.mainloop()

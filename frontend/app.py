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
from backend import usb_manager   # listar, verificar, formatear
from backend import utils         # restaurar_respaldo, log_event

def mostrar_dispositivos():
    """
    Lista los dispositivos USB conectados y los muestra en la caja de texto.
    """
    salida = usb_manager.listar_dispositivos()
    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, salida)

def verificar():
    """
    Verifica el estado del dispositivo USB ingresado en la entrada.
    """
    device = entry_device.get()
    resultado = usb_manager.verificar_usb(device)
    messagebox.showinfo("Resultado", resultado)

def formatear():
    """
    Formatea el dispositivo USB ingresado en la entrada.
    """
    device = entry_device.get()
    resultado = usb_manager.formatear_usb(device)
    messagebox.showinfo("Resultado", resultado)

def restaurar():
    """
    Restaura un respaldo desde la carpeta 'respaldo' hacia el dispositivo seleccionado.
    """
    origen = "respaldo"
    destino = f"/media/{entry_device.get()}"
    resultado = utils.restaurar_respaldo(origen, destino)
    messagebox.showinfo("Resultado", resultado)

# Ventana principal
root = tk.Tk()
root.title("Gestor de USB Cyberpunk")
root.geometry("800x500")
root.configure(bg="#7c7c7c")  # fondo 

# Frame superior: entrada de dispositivo
top_frame = ttk.Frame(root, padding=20)
top_frame.pack(fill="x")

ttk.Label(top_frame, text="Dispositivo (ej. sda1):",
          font=("Consolas", 14),
          foreground="#08f514", background="#7c7c7c").grid(row=0, column=0, padx=5)
entry_device = ttk.Entry(top_frame, font=("Consolas", 14))
entry_device.grid(row=0, column=1, padx=5)

# Frame de botones
btn_frame = tk.Frame(root, bg="#7c7c7c")
btn_frame.pack(pady=10)

style = ttk.Style()
style.configure("Cyber.TButton",
                font=("Consolas", 12),
                foreground="#af00ff",
                background="#000000")

ttk.Button(btn_frame, text="📂 Listar", style="Cyber.TButton",
           command=mostrar_dispositivos).grid(row=0, column=0, padx=10)
ttk.Button(btn_frame, text="🔍 Verificar", style="Cyber.TButton",
           command=verificar).grid(row=0, column=1, padx=10)
ttk.Button(btn_frame, text="⚡ Formatear", style="Cyber.TButton",
           command=formatear).grid(row=0, column=2, padx=10)
ttk.Button(btn_frame, text="♻️ Restaurar", style="Cyber.TButton",
           command=restaurar).grid(row=0, column=3, padx=10)

# Frame inferior: caja de texto estilo terminal
bottom_frame = ttk.Frame(root, padding=20)
bottom_frame.pack(fill="both", expand=True)

text_box = tk.Text(bottom_frame, height=15,
                   font=("Consolas", 12),
                   fg="#af00ff", bg="#000000",
                   insertbackground="#08f514")
text_box.pack(fill="both", expand=True)

root.mainloop()

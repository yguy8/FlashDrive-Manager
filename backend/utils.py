"""
utils.py
Funciones auxiliares para:
- Registrar logs
- Crear y restaurar respaldos
- Listar archivos
"""

import os
import shutil
import datetime

def log_event(message, logfile="usb_log.txt"):
    """Registra eventos en un archivo de log con fecha y hora"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(logfile, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

def crear_respaldo(origen, destino):
    """Copia archivos desde origen a destino como respaldo"""
    try:
        if not os.path.exists(destino):
            os.makedirs(destino)
        shutil.copytree(origen, destino, dirs_exist_ok=True)
        log_event(f"Respaldo creado de {origen} a {destino}")
        return f"Respaldo creado en {destino}"
    except Exception as e:
        log_event(f"Error al crear respaldo: {e}")
        return f"Error: {e}"

def restaurar_respaldo(origen, destino):
    """Restaura archivos desde respaldo al dispositivo destino"""
    try:
        shutil.copytree(origen, destino, dirs_exist_ok=True)
        log_event(f"Respaldo restaurado de {origen} a {destino}")
        return f"Respaldo restaurado en {destino}"
    except Exception as e:
        log_event(f"Error al restaurar respaldo: {e}")
        return f"Error: {e}"

def listar_archivos(ruta):
    """Devuelve lista de archivos en una ruta"""
    try:
        return os.listdir(ruta)
    except Exception as e:
        log_event(f"Error al listar archivos en {ruta}: {e}")
        return []

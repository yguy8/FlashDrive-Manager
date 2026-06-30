"""
usb_manager.py
Módulo para gestionar memorias USB:
- Listar dispositivos conectados
- Verificar con fsck
- Formatear con mkfs
"""

import subprocess
import backend.utils as utils

def listar_dispositivos():
    """Devuelve lista de dispositivos USB conectados"""
    try:
        result = subprocess.run(
            ["lsblk", "-o", "NAME,SIZE,MOUNTPOINT"],
            capture_output=True,
            text=True,
            check=True
        )
        utils.log_event("Dispositivos listados correctamente")
        return result.stdout
    except subprocess.CalledProcessError as e:
        utils.log_event(f"Error al listar dispositivos: {e}")
        return f"Error: {e}"

def verificar_usb(device):
    """Ejecuta fsck para verificar errores en el dispositivo"""
    try:
        subprocess.run(["fsck", f"/dev/{device}"], check=True)
        utils.log_event(f"Verificación exitosa en {device}")
        return f"Dispositivo {device} verificado correctamente."
    except subprocess.CalledProcessError as e:
        utils.log_event(f"Error al verificar {device}: {e}")
        return f"Error al verificar {device}: {e}"

def formatear_usb(device, sistema="vfat"):
    """Formatea el dispositivo con el sistema de archivos indicado"""
    try:
        subprocess.run(["mkfs", f"-t{sistema}", f"/dev/{device}"], check=True)
        utils.log_event(f"Formateo exitoso en {device} como {sistema}")
        return f"Dispositivo {device} formateado como {sistema}."
    except subprocess.CalledProcessError as e:
        utils.log_event(f"Error al formatear {device}: {e}")
        return f"Error al formatear {device}: {e}"

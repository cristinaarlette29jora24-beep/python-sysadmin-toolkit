import os
import shutil
import subprocess
from typing import List

def check_ping(ip: str) -> bool:
    """Ejecuta un ping hacia una IP o dominio y devuelve True si responde."""
    # Nota de administración: Usamos '-n 1' si estás en Windows. Si usas Linux en tu servidor CEAC, cámbialo a '-c 1'
    comando: List[str] = ["ping", "-n", "1", ip]
    try:
        resultado = subprocess.run(
            comando, 
            stdout=subprocess.DEVNULL, 
            stderr=subprocess.DEVNULL, 
            text=True, 
            timeout=5
        )
        return resultado.returncode == 0
    except subprocess.TimeoutExpired:
        return False

def check_disk_space(ruta: str = "C:\\") -> float:
    """Comprueba el espacio libre en disco y lanza una alerta si es menor al 20%."""
    # Nota: Si estás en Linux cambias "C:\\" por la raíz "/"
    total, usado, libre = shutil.disk_usage(ruta)
    porcentaje_libre: float = (libre / total) * 100
    
    print(f"\n📊 Análisis de disco en '{ruta}':")
    print(f"   Total: {total / (1024**3):.2f} GB")
    print(f"   Libre: {libre / (1024**3):.2f} GB ({porcentaje_libre:.2f}%)")
    
    if porcentaje_libre < 20.0:
        print(f"🚨 ¡ALERTA CRÍTICA: El espacio libre en '{ruta}' es inferior al 20%!")
    else:
        print("✅ El espacio en disco está en niveles seguros.")
        
    return porcentaje_libre
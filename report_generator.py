import os
from datetime import datetime
import shutil
import platform
import uuid
import log_parser

def crear_informe_completo() -> None:
    print("\n💾 Generando informe consolidado del sistema...")
    
    # Asegurar que la carpeta data existe
    os.makedirs("data", exist_ok=True)
    
    fecha_hoy = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    ruta_informe = f"data/informe_{fecha_hoy}.txt"
    
    # Obtener datos de disco para el informe
    total, usado, libre = shutil.disk_usage("/")
    disco_libre_gb = libre / (1024 ** 3)
    
    # Obtener datos de hardware
    mac_ficticia = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1]).upper()
    
    with open(ruta_informe, "w", encoding="utf-8") as f:
        f.write("==================================================\n")
        f.write("      INFORME AUTOMÁTICO DE AUDITORÍA Y SISTEMA   \n")
        f.write(f"      Generado el: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
        f.write("==================================================\n\n")
        
        # 1. Seguridad
        f.write("🚨 1. AUDITORÍA DE SEGURIDAD SSH\n")
        f.write("-" * 40 + "\n")
        fallos = log_parser.analizar_intentos_fallidos()
        if fallos:
            for ip, intentos in fallos.items():
                f.write(f"💀 IP Sospechosa: {ip:<15} | Intentos fallidos: {intentos}\n")
        else:
            f.write("✅ Sin alertas activas en auth.log.\n")
        f.write("\n")
        
        # 2. Almacenamiento
        f.write("💾 2. ESTADO DEL ALMACENAMIENTO\n")
        f.write("-" * 40 + "\n")
        f.write(f" Espacio libre en disco principal: {disco_libre_gb:.2f} GB\n\n")
        
        # 3. Hardware
        f.write("🖥️  3. INVENTARIO DE HARDWARE\n")
        f.write("-" * 40 + "\n")
        f.write(f" Sistema Operativo : {platform.system()} {platform.release()}\n")
        f.write(f" Procesador        : {platform.processor()}\n")
        f.write(f" Dirección MAC     : {mac_ficticia}\n\n")
        
        f.write("==================================================\n")
        f.write("            FIN DEL INFORME - TODO OK             \n")
        f.write("==================================================\n")
        
    print(f"📝 ¡Perfecto! Tu reporte completo se ha guardado en: '{ruta_informe}'")
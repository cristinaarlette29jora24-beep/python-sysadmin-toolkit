import platform
import uuid

def obtener_inventario_sistema() -> None:
    print("\n🖥️  GENERANDO INVENTARIO DE HARDWARE Y SISTEMA")
    print("-" * 50)
    
    # Extraemos la información del OS y la arquitectura
    print(f" ⚙️  Sistema Operativo : {platform.system()} {platform.release()}")
    print(f" 📁 Arquitectura      : {platform.machine()}")
    print(f" 🧠 Procesador        : {platform.processor()}")
    
    # Extraemos el identificador único físico (Dirección MAC) de forma limpia
    mac_ficticia = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1])
    print(f" 🆔 Dirección MAC (Física): {mac_ficticia.upper()}")
    print("-" * 50)
    print("✅ Datos del sistema recolectados con éxito.")
import os
from typing import Dict, Set

def analizar_intentos_fallidos(ruta_log: str = "logs/auth.log") -> Dict[str, int]:
    """Lee el archivo de log línea a línea y cuenta fallos por cada IP."""
    conteo_fallidos: Dict[str, int] = {}
    
    if not os.path.exists(ruta_log):
        print(f"❌ Error: No se encuentra el archivo de log en '{ruta_log}'")
        return conteo_fallidos

    # 'with open' asegura que el archivo se cierre solo y no sature la RAM
    with open(ruta_log, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            # Buscamos la cadena típica de intento fallido en entornos Linux
            if "Failed password" in linea:
                partes = linea.split()
                if "from" in partes:
                    # Buscamos la posición de la IP, que va justo después de 'from'
                    indice_ip = partes.index("from") + 1
                    ip = partes[indice_ip]
                    # Sumamos 1 al contador de esa IP exacta
                    conteo_fallidos[ip] = conteo_fallidos.get(ip, 0) + 1
                    
    return conteo_fallidos

def ejecutar_auditoria() -> None:
    print("\n🔍 Analizando registros de seguridad en logs/auth.log...")
    resultados = analizar_intentos_fallidos()
    
    if not resultados:
        print("✅ No se detectaron anomalías ni intentos fallidos de login.")
        return
        
    print("\n🚨 ¡ALERT! IPs sospechosas detectadas intentando forzar SSH:")
    print("-" * 45)
    for ip, intentos in resultados.items():
        print(f" 💀 Dirección IP: {ip:<15} | Intentos fallidos: {intentos}")
    print("-" * 45)
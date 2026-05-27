# threat_intel.py
import requests
from typing import Dict, Any

def geolocalizar_ip(ip: str) -> Dict[str, Any]:
    """
    Hace una petición a la API de ipinfo.io para obtener la ubicación
    y la organización proveedora de internet de una IP sospechosa.
    """
    # Usamos un timeout de 5 segundos para que el script no se quede colgado si falla la red
    url: str = f"https://ipinfo.io/{ip}/json"
    
    try:
        respuesta = requests.get(url, timeout=5)
        # Si la API devuelve un código de error (como 404 o 500), salta al except
        respuesta.raise_for_status() 
        
        datos: Dict[str, Any] = respuesta.json()
        return datos
        
    except requests.RequestException:
        # Si no hay internet o la API falla, devolvemos un diccionario con datos seguros por defecto
        return {"country": "Desconocido", "org": "Error de conexión con la API"}

def mostrar_tabla_ataques(conteo_ips: Dict[str, int]) -> None:
    """
    Recibe el diccionario de IPs atacantes del log y muestra en consola
    una tabla ejecutiva con su geolocalización.
    """
    print("\n" + "="*85)
    print(f"{'IP ATACANTE':<18} | {'INTENTOS':<10} | {'PAÍS':<8} | {'ORGANIZACIÓN / ISP'}")
    print("="*85)
    
    for ip, intentos in conteo_ips.items():
        # Llamamos a la API para cada IP
        info_geo = geolocalizar_ip(ip)
        pais = info_geo.get("country", "N/A")
        organizacion = info_geo.get("org", "N/A")
        
        print(f"{ip:<18} | {intentos:<10} | {pais:<8} | {organizacion}")
    
    print("="*85 + "\n")
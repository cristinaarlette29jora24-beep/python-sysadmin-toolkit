import sys
from typing import NoReturn
import os_utils
import log_parser
import network_inventory
import report_generator  # <-- Nueva importación

def mostrar_menu() -> None:
    print("\n" + "="*45)
    print("🛠️  SYSADMIN TOOLKIT INTERACTIVO - FINAL")
    print("="*45)
    print("1. Verificar conectividad de red (Ping)")
    print("2. Comprobar espacio libre en disco")
    print("3. Analizar logs de SSH (auth.log)")
    print("4. Generar Inventario de Hardware")
    print("5. Exportar Informe de Auditoría (Nuevo)")  # <-- Nueva opción
    print("6. Salir")
    print("="*45)

def ejecutar_opcion(opcion: str) -> None:
    if opcion == "1":
        ip = input("Introduce la IP o dominio a testear (ej. 8.8.8.8): ").strip()
        print(f"⏳ Enviando paquete a {ip}...")
        if os_utils.check_ping(ip):
            print(f"✅ ¡Conectividad exitosa! {ip} responde.")
        else:
            print(f"❌ Fallo de red: {ip} no responde.")
            
    elif opcion == "2":
        os_utils.check_disk_space()
        
    elif opcion == "3":
        log_parser.ejecutar_auditoria()
        
    elif opcion == "4":
        network_inventory.obtener_inventario_sistema()
        
    elif opcion == "5":
        # Ejecutamos el nuevo exportador
        report_generator.crear_informe_completo()
        
    elif opcion == "6":
        print("Cerrando sesión en el Toolkit. ¡Buen trabajo, Admin!")
        sys.exit(0)
    else:
        print("⚠ Opción no válida. Selecciona una opción del 1 al 6.")

def main() -> NoReturn:
    while True:
        mostrar_menu()
        seleccion = input("Selecciona una opción: ").strip()
        ejecutar_opcion(seleccion)

if __name__ == "__main__":
    main()
import csv
import random
from faker import Faker
from typing import Optional

fake = Faker("es_ES")

SISTEMAS_OPERATIVOS = [
    "Windows Server 2019", "Windows Server 2022",
    "Ubuntu 22.04 LTS", "Ubuntu 20.04 LTS",
    "CentOS 7", "Debian 11", "Red Hat 8"
]
DEPARTAMENTOS = ["IT", "RRHH", "Finanzas", "Logística", "Marketing", "Operaciones", "Dirección"]
ROLES = ["Web Server", "DB Server", "File Server", "Mail Server", "Proxy", "Backup", "DNS"]

def generar_csv_inventario(ruta_salida: str = "inventory.csv", total_filas: int = 1000) -> None:
    print(f"⚙️  Generando inventario con {total_filas} servidores ficticios...")
    with open(ruta_salida, "w", newline="", encoding="utf-8") as f:
        campos = ["hostname", "ip", "mac", "sistema_operativo", "ram_gb", "departamento", "rol"]
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        for i in range(total_filas):
            writer.writerow({
                "hostname": f"SRV-{fake.lexify('???').upper()}-{i+1:04d}",
                "ip": fake.ipv4_private(),
                "mac": fake.mac_address().upper(),
                "sistema_operativo": random.choice(SISTEMAS_OPERATIVOS),
                "ram_gb": random.choice([2, 4, 8, 16, 32, 64]),
                "departamento": random.choice(DEPARTAMENTOS),
                "rol": random.choice(ROLES),
            })
    print(f"✅ Inventario guardado en '{ruta_salida}' con {total_filas} registros.")

if __name__ == "__main__":
    generar_csv_inventario()

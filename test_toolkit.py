# test_toolkit.py
import pytest
from typing import Dict

# Función de prueba simplificada basada en tu log_parser.py
def contar_fallos_lineas(lineas: list[str]) -> Dict[str, int]:
    conteo: Dict[str, int] = {}
    for linea in lineas:
        if "Failed password" in linea:
            partes = linea.split()
            # En un auth.log estándar, la IP suele estar después de 'from'
            if "from" in partes:
                idx = partes.index("from") + 1
                if idx < len(partes):
                    ip = partes[idx]
                    conteo[ip] = conteo.get(ip, 0) + 1
    return conteo

def test_conteo_ips_atacantes() -> None:
    logs_simulados = [
        "May 26 21:10:05 srv-ssh sshd[1234]: Failed password for invalid user admin from 192.168.1.50 port 43210 ssh2",
        "May 26 21:11:02 srv-ssh sshd[1234]: Accepted password for root from 192.168.1.10 port 54321 ssh2",
        "May 26 21:12:15 srv-ssh sshd[1234]: Failed password for invalid user root from 192.168.1.50 port 43215 ssh2"
    ]
    
    resultado = contar_fallos_lineas(logs_simulados)
    
    # La IP .50 tiene que tener 2 fallos, y la .10 ninguno porque fue exitoso (Accepted)
    assert resultado["192.168.1.50"] == 2
    assert "192.168.1.10" not in resultado
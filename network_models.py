# network_models.py
from abc import ABC, abstractmethod

class NetworkDevice(ABC):
    """Clase base abstracta para representar cualquier dispositivo de red."""
    
    def __init__(self, hostname: str, ip: str, mac: str) -> None:
        self.hostname: str = hostname
        self.ip: str = ip
        self.mac: str = mac

    @abstractmethod
    def audit_device(self) -> None:
        """Método abstracto que cada tipo de dispositivo debe implementar."""
        pass


class Router(NetworkDevice):
    """Clase hija que representa un Router de la infraestructura."""
    
    def __init__(self, hostname: str, ip: str, mac: str, interfaces_activas: int) -> None:
        super().__init__(hostname, ip, mac)
        self.interfaces_activas: int = interfaces_activas

    def audit_device(self) -> None:
        print(f"\n🛡️  [AUDITORÍA ROUTER] -> Evaluando {self.hostname} ({self.ip})")
        print(f"   -> Verificando tablas de enrutamiento en dirección MAC: {self.mac}")
        print(f"   -> Alerta: Revisar que las {self.interfaces_activas} interfaces tengan ACLs aplicadas.")


class Server(NetworkDevice):
    """Clase hija que representa un Servidor de producción."""
    
    def __init__(self, hostname: str, ip: str, mac: str, sistema_operativo: str) -> None:
        super().__init__(hostname, ip, mac)
        self.sistema_operativo: str = sistema_operativo

    def audit_device(self) -> None:
        print(f"\n🖥️  [AUDITORÍA SERVIDOR] -> Evaluando {self.hostname} ({self.ip})")
        print(f"   -> Sistema Operativo detectado: {self.sistema_operativo}")
        print(f"   -> Alerta SecOps: Comprobar parches críticos de seguridad y accesos SSH en {self.mac}")
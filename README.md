# 🛠️ Python SysAdmin Toolkit
 
Kit de herramientas CLI en Python para la automatización de administración de sistemas.
 
![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python) ![pytest](https://img.shields.io/badge/tests-1%20passed-brightgreen?logo=pytest) ![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?logo=pandas) ![License](https://img.shields.io/badge/licencia-académica-lightgrey)
 
---
 
## 📌 Descripción
 
Suite modular de scripts Python orientada a administradores de sistemas que automatiza tareas críticas: auditoría de seguridad SSH, control de almacenamiento, modelado de inventario de red con POO, inteligencia de amenazas vía API, procesamiento masivo de datos con Pandas y generación de informes ejecutivos en Excel.
 
Desarrollado como entregable de la **Fase 7 — Automatización y análisis de redes con Python** del ciclo ASIR.
 
---
 
## ✨ Características
 
- Auditoría de logs SSH con detección de IPs atacantes
- Control de espacio en disco con alertas automáticas
- Modelado de red con clases `NetworkDevice`, `Router` y `Server` (POO + polimorfismo)
- Geolocalización de IPs sospechosas con la API de [ipinfo.io](https://ipinfo.io)
- Generación de inventario CSV de 1000+ servidores ficticios con Faker
- Filtrado y agrupación de inventario por departamento con Pandas
- Exportación de informes ejecutivos a Excel con estilos corporativos
- Demonio de automatización que ejecuta el ciclo completo cada hora
- Tests unitarios con pytest
---
 
## 🛠️ Tecnologías
 
| Módulo | Tecnología | Uso |
|---|---|---|
| Sistema operativo | `subprocess`, `shutil` | Ping, control de disco |
| Parseo de logs | `re`, `set`, `dict` | Auditoría SSH |
| Modelado de red | `abc`, POO | Clases de dispositivos |
| Inteligencia de amenazas | `requests` | API REST ipinfo.io |
| Inventario | `faker`, `csv`, `random` | Generación de datos |
| Análisis de datos | `pandas` | Filtrado y agrupación |
| Informes | `openpyxl` | Exportación a Excel |
| Automatización | `schedule` | Demonio periódico |
| Testing | `pytest` | Tests unitarios |
 
---
 
## 📁 Estructura del proyecto
 
```
python-sysadmin-toolkit/
│
├── sys_toolkit.py            # Menú CLI principal con type hints
├── os_utils.py               # Ping con subprocess y control de disco
├── log_parser.py             # Parseo de auth.log — auditoría SSH
├── network_models.py         # POO: clases NetworkDevice, Router, Server
├── network_inventory.py      # Inventario de dispositivos de red
├── threat_intel.py           # Integración API ipinfo.io
├── generate_inventory.py     # Generador CSV con Faker (1000 filas)
├── inventory_manager.py      # Análisis de inventario con Pandas
├── excel_reporter.py         # Informes ejecutivos a Excel
├── scheduler_daemon.py       # Demonio con schedule (cada hora)
├── test_toolkit.py           # Tests unitarios con pytest
│
├── logs/
│   └── auth.log              # Log SSH de prueba
├── data/                     # Informes Excel generados (ignorado en git)
├── docs/
│   └── python-sysadmin.md    # Documentación técnica
│
├── requirements.txt
├── .gitignore
└── README.md
```
 
---
 
## ⚡ Inicio rápido
 
```bash
git clone https://github.com/cristinaarlette29jora24-beep/python-sysadmin-toolkit.git
cd python-sysadmin-toolkit
```
 
```bash
# Linux / macOS
python3 -m venv venv
source venv/bin/activate
 
# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1
```
 
```bash
pip install -r requirements.txt
```
 
Abre el menú interactivo:
 
```bash
python sys_toolkit.py
```
 
---
 
## 🚀 Uso de módulos individuales
 
```bash
# Auditoría SSH — detectar IPs atacantes en auth.log
python log_parser.py
 
# Geolocalizar IPs sospechosas con ipinfo.io
python threat_intel.py
 
# Generar inventario de 1000 servidores ficticios
python generate_inventory.py
 
# Filtrar y agrupar inventario con Pandas
python inventory_manager.py
 
# Exportar informe ejecutivo a Excel
python excel_reporter.py
 
# Activar demonio (ejecuta el ciclo completo cada hora)
python scheduler_daemon.py
```
 
---
 
## 🧪 Tests
 
```bash
python -m pytest test_toolkit.py -v
```
 
```
platform win32 -- Python 3.14.5, pytest-9.0.3
collected 1 item
 
test_toolkit.py::test_conteo_ips_atacantes PASSED    [100%]
 
1 passed in 0.28s
```
 
---
 
## 📄 Documentación
 
| Documento | Descripción |
|---|---|
| [`docs/python-sysadmin.md`](docs/python-sysadmin.md) | Por qué Python además de Bash en ASIR |
| [`requirements.txt`](requirements.txt) | Dependencias del proyecto |
 
---
 
*Desarrollado por Trinidad · Ciclo ASIR · CEAC Valencia · 2025-2026*
# scheduler_daemon.py
import time
import schedule
from generate_inventory import generar_csv_inventario
from inventory_manager import procesar_inventario
from excel_reporter import exportar_a_excel_ejecutivo

def tarea_mensual_automatizada() -> None:
    print(f"\n⏰ [DEMONIO] Iniciando ejecución programada automática: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    # 1. Regenerar o leer último inventario
    generar_csv_inventario("inventory.csv", total_filas=1000)
    # 2. Filtrar con pandas
    df_criticos, _ = procesar_inventario("inventory.csv")
    # 3. Lanzar reporte excel pulido
    exportar_a_excel_ejecutivo(df_criticos, ruta_salida="data/informe_ejecutivo_mensual.xlsx")
    print("⏰ [DEMONIO] Tarea completada con éxito. Esperando próximo ciclo...")

# Programamos para que corra cada hora como pide la rúbrica
schedule.every().hour.do(tarea_mensual_automatizada)

# Nota didáctica: Si quieres probarlo en vivo ante el tutor, descomenta la línea de abajo para que corra cada 10 segundos:
# schedule.every(10).seconds.do(tarea_mensual_automatizada)

if __name__ == "__main__":
    print("🚀 Demonio de administración Python activado. Presiona Ctrl+C para detenerlo...")
    # Bucle infinito para mantener el script corriendo en segundo plano en tu servidor
    while True:
        schedule.run_pending()
        time.sleep(1)
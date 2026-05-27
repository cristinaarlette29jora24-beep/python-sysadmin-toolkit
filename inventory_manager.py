import pandas as pd
from typing import Tuple

def procesar_inventario(ruta_csv: str = "inventory.csv") -> Tuple[pd.DataFrame, pd.DataFrame]:
    try:
        df = pd.read_csv(ruta_csv, encoding="utf-8")
    except FileNotFoundError:
        print(f"❌ No se encuentra '{ruta_csv}'. Genera primero el inventario.")
        return pd.DataFrame(), pd.DataFrame()

    print(f"\n📂 Inventario cargado: {len(df)} servidores totales.")

    df_criticos = df[
        (df["sistema_operativo"].str.contains("Windows Server", na=False)) |
        (df["ram_gb"] < 4)
    ].copy()

    print(f"⚠️  Servidores críticos detectados: {len(df_criticos)}")

    agrupacion = df.groupby("departamento")["hostname"].count().reset_index()
    agrupacion.columns = ["Departamento", "Total Servidores"]
    agrupacion = agrupacion.sort_values("Total Servidores", ascending=False)

    print("\n📊 Servidores por departamento:")
    print(agrupacion.to_string(index=False))

    return df_criticos, agrupacion

if __name__ == "__main__":
    procesar_inventario()

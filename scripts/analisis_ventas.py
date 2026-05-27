"""Análisis de ventas - TP Organización Empresarial.

Lee el archivo de ventas, calcula indicadores básicos
(ventas totales, producto más vendido, ventas por mes) y
genera un gráfico de la evolución mensual de ventas.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "datos" / "sales_sample_2024.csv"
RESULTS_DIR = ROOT / "resultados"


def cargar_ventas(ruta: Path) -> pd.DataFrame:
    return pd.read_csv(ruta, parse_dates=["sales_date"])


def ventas_totales(df: pd.DataFrame) -> float:
    return float(df["sales_amount"].sum())


def ventas_por_producto(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("producto")
        .agg(
            cantidad_ventas=("sales_amount", "count"),
            monto_total=("sales_amount", "sum"),
        )
        .sort_values("cantidad_ventas", ascending=False)
    )


def ventas_por_mes(df: pd.DataFrame) -> pd.Series:
    return (
        df.set_index("sales_date")["sales_amount"]
        .resample("MS")
        .sum()
    )


def graficar_evolucion(serie: pd.Series, destino: Path) -> None:
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(serie.index, serie.values, marker="o", linewidth=2)
    ax.set_title("Evolución de ventas mensuales - 2024")
    ax.set_xlabel("Mes")
    ax.set_ylabel("Ventas ($)")
    ax.grid(True, alpha=0.3)
    fig.autofmt_xdate()
    fig.tight_layout()
    fig.savefig(destino, dpi=120)
    plt.close(fig)


def main() -> None:
    df = cargar_ventas(DATA_FILE)

    total = ventas_totales(df)
    por_producto = ventas_por_producto(df)
    mensual = ventas_por_mes(df)

    producto_top = por_producto.index[0]
    cantidad_top = por_producto.loc[producto_top, "cantidad_ventas"]
    monto_top = por_producto.loc[producto_top, "monto_total"]

    print("=" * 50)
    print("REPORTE DE VENTAS 2024")
    print("=" * 50)
    print(f"\nVentas totales: ${total:,.0f}")
    print(
        f"\nProducto más vendido: {producto_top} "
        f"({cantidad_top} ventas, ${monto_top:,.0f})"
    )
    print("\nVentas por producto:")
    print(por_producto.to_string())
    print("\nVentas por mes:")
    for fecha, monto in mensual.items():
        print(f"  {fecha:%Y-%m}: ${monto:,.0f}")

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    grafico = RESULTS_DIR / "evolucion_ventas.png"
    graficar_evolucion(mensual, grafico)
    print(f"\nGráfico guardado en: {grafico}")


if __name__ == "__main__":
    main()

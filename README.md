# TP - Organización Empresarial: Análisis de Ventas

Trabajo práctico de la materia **Organización Empresarial**. El objetivo es
analizar la información de ventas de una empresa y generar indicadores básicos
que permitan interpretar su desempeño durante el año.

## Integrantes del equipo

- Franco Aglieri

## Escenario elegido

**Análisis de ventas de una empresa durante el año 2024.**

A partir de un registro diario de ventas se calculan indicadores que ayudan a
interpretar el desempeño comercial:

- Ventas totales del año.
- Producto más vendido.
- Ventas agrupadas por mes.
- Gráfico de la evolución mensual de las ventas.

## Dataset utilizado

El dataset base fue obtenido del siguiente gist público:

<https://gist.github.com/khanusama20/ee33c2869dd5cf3cebdf020be1ca43f6>

El archivo original contiene un registro diario de ventas del año 2024 con las
columnas `id`, `sales_date` y `sales_amount`. Para cumplir con los requisitos
del trabajo se **adaptó el dataset agregando una columna `producto` al final**,
distribuyendo los siguientes productos a lo largo del año:

- Mouse
- Teclado
- Auriculares
- Monitor
- Notebook
- Webcam

La distribución se eligió de forma que algunos productos se repiten más que
otros, lo que permite identificar claramente al producto más vendido.

El archivo final se encuentra en `datos/sales_sample_2024.csv` y tiene las
siguientes columnas:

| Columna       | Descripción                          |
| ------------- | ------------------------------------ |
| `id`          | Identificador único de la venta      |
| `sales_date`  | Fecha de la venta (YYYY-MM-DD)       |
| `sales_amount`| Monto de la venta                    |
| `producto`    | Producto vendido (agregado en el TP) |

## Estructura del proyecto

```
tp-organizacion/
├── datos/
│   └── sales_sample_2024.csv     # Dataset de ventas
├── scripts/
│   └── analisis_ventas.py        # Script de análisis
├── resultados/
│   ├── evolucion_ventas.png      # Gráfico generado por el script
│   └── reporte_ventas.txt        # Reporte de indicadores en texto
└── README.md
```

## Requisitos

- Python 3.10 o superior
- Librerías: `pandas` y `matplotlib`

Instalación de dependencias:

```bash
pip install pandas matplotlib
```

## Cómo ejecutar el script

Desde la raíz del proyecto:

```bash
python3 scripts/analisis_ventas.py
```

El script:

1. Lee el archivo `datos/sales_sample_2024.csv`.
2. Imprime en consola los indicadores calculados (ventas totales, producto
   más vendido, ventas por mes).
3. Guarda el mismo reporte en `resultados/reporte_ventas.txt`.
4. Genera el gráfico de evolución mensual de ventas en
   `resultados/evolucion_ventas.png`.

# ejercicio03.py
import pandas as pd
import numpy as np

def main():
    # Leer el archivo CSV
    df = pd.read_csv("ventas.csv")

    # Asegurar que Total sea numérico
    df['Total'] = pd.to_numeric(df['Total'], errors='coerce')

    # Reglas del descuento:
    # Si Total >= 1000 → 10%
    # Si Total >= 500  → 5%
    # Si Total < 500   → 0%
    df['Descuento'] = np.where(df['Total'] >= 1000, 0.10,
                        np.where(df['Total'] >= 500, 0.05, 0.0))

    # Calcular el total con el descuento aplicado
    df['Total_con_descuento'] = (df['Total'] * (1 - df['Descuento'])).round(2)

    # Mostrar las primeras filas
    print(df[['Cliente','Producto','Total','Descuento','Total_con_descuento']].head(10))

    # Guardar archivo nuevo
    df.to_csv("ejercicio03_descuentos.csv", index=False)
    print("\nArchivo guardado: ejercicio03_descuentos.csv")

if __name__ == "__main__":
    main()

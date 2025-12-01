# ejercicio05
import pandas as pd
import numpy as np

def main():
    df = pd.read_csv("ventas.csv")
    df = df.copy()

    # asegurar Total numérico
    df['Total'] = pd.to_numeric(df['Total'], errors='coerce').fillna(0)

    # Impuesto: supongamos 15% sobre Total
    df['Impuesto'] = (df['Total'] * 0.15).round(2)
    df['Total_Final'] = (df['Total'] + df['Impuesto']).round(2)

    # Clasificación por percentiles o por rangos fijos:
    # usar percentiles para adaptación automática
    low = df['Total_Final'].quantile(0.33)
    high = df['Total_Final'].quantile(0.66)

    def clasificar(x):
        if x <= low:
            return "Bajo"
        elif x <= high:
            return "Medio"
        else:
            return "Alto"

    df['Rango_Total'] = df['Total_Final'].apply(clasificar)

    print(df[['Cliente','Producto','Total','Impuesto','Total_Final','Rango_Total']].head(10))
    df.to_csv("ejercicio05_impuesto_clasificado.csv", index=False)
    print("\nGuardado: ejercicio05_impuesto_clasificado.csv")

if __name__ == "__main__":
    main()

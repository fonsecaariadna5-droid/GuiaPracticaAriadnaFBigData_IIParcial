# ejercicio04
import pandas as pd
import numpy as np

def safe_to_numeric(s):
    return pd.to_numeric(s, errors='coerce')

def main():
    df = pd.read_csv("ventas.csv")
    df = df.copy()

    cols = []
    for c in ['Cantidad', 'Precio_Unitario', 'Total']:
        if c in df.columns:
            cols.append(c)
    if not cols:
        print("No encontré las columnas esperadas. Edita el script según tu CSV.")
        return

    # convertir y contar no-numéricos
    for c in cols:
        before_non_numeric = df[c].apply(lambda x: pd.to_numeric(x, errors='coerce')).isna().sum()
        df[c] = safe_to_numeric(df[c])
        after_non_numeric = df[c].isna().sum()
        print(f"Columna {c}: valores convertidos, NaNs después de conversión: {after_non_numeric}")

    # reemplazar NaNs por promedios (por columna)
    for c in cols:
        if df[c].isna().any():
            mean_val = df[c].mean()
            df[c] = df[c].fillna(mean_val)
            print(f"Reemplazados NaN en {c} por promedio {mean_val}")

    # recalcular Total si falta o es inconsistente: Total = Cantidad * Precio_Unitario
    if set(['Cantidad','Precio_Unitario']).issubset(df.columns):
        df['Total_calc'] = (df['Cantidad'] * df['Precio_Unitario']).round(2)
        # si la diferencia absoluta supera 0.01, corregimos Total con Total_calc
        if 'Total' in df.columns:
            diff = (df['Total'] - df['Total_calc']).abs()
            mask = diff > 0.01
            corrected = mask.sum()
            df.loc[mask, 'Total'] = df.loc[mask, 'Total_calc']
            print(f"Se corrigieron {corrected} registros de Total usando Cantidad*Precio_Unitario")
        else:
            df['Total'] = df['Total_calc']

        df = df.drop(columns=['Total_calc'])

    df.to_csv("ejercicio04_tipos_corregidos.csv", index=False)
    print("Guardado: ejercicio04_tipos_corregidos.csv")

if __name__ == "__main__":
    main()

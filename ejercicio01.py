# ejercicio01

import pandas as pd

def main():
    df = pd.read_csv("ventas.csv")
    print("Registros iniciales:", len(df))

    # detectar nulos por columna
    print("\nNulos por columna:\n", df.isnull().sum())

    # eliminar nulos
    df_clean = df.dropna()
    print("\nRegistros después de eliminar nulos:", len(df_clean))

    # eliminar duplicados (todas las columnas)
    df_clean = df_clean.drop_duplicates()
    print("Registros después de eliminar duplicados:", len(df_clean))

    # guardar resultado opcional
    df_clean.to_csv("ejercicio01_ventas_limpias.csv", index=False)
    print("\nGuardado: ejercicio01_ventas_limpias.csv")

if __name__ == "__main__":
    main()

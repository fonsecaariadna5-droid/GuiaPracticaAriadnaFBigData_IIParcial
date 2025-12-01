# ejercicio02
import pandas as pd

def normalize_text(s):
    if pd.isna(s):
        return s
    return str(s).strip().title()   # Limpia y pone primeras letras en mayúscula

def main():
    # Cargar CSV
    df = pd.read_csv("ventas.csv", dtype=str)

    # Quitar espacios en nombres de columnas
    df.columns = df.columns.str.strip()

    # Verificar columnas existentes
    cols = []
    if "Cliente" in df.columns:
        cols.append("Cliente")
    if "Producto" in df.columns:
        cols.append("Producto")

    if not cols:
        print(" No encontré 'Cliente' ni 'Producto' en el CSV.")
        print("Columnas encontradas:", list(df.columns))
        return

    print("Valores ANTES:")
    print(df[cols].head(10))

    # Normalizar texto
    df_norm = df.copy()
    for c in cols:
        df_norm[c] = df_norm[c].apply(normalize_text)

    print("\nValores DESPUÉS:")
    print(df_norm[cols].head(10))

    # Guardar archivo limpio
    df_norm.to_csv("ejercicio02_ventas_normalizadas.csv", index=False)
    print("\n Archivo guardado: ejercicio02_ventas_normalizadas.csv")

if __name__ == "__main__":
    main()

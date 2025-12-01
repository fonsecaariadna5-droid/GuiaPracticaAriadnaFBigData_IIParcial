# ejercicio06
import pandas as pd

def main():
    df = pd.read_csv("ventas.csv")
    df['Total'] = pd.to_numeric(df['Total'], errors='coerce').fillna(0)

    # pedir umbral por consola (opcional) o usar 0
    umbral = float(input("Filtrar registros con Total >= (ej: 100): ") or 0)

    df_filtered = df[df['Total'] >= umbral].sort_values('Total', ascending=False)
    print(df_filtered.head(20))
    df_filtered.to_csv("ejercicio06_filtrado_ordenado.csv", index=False)
    print("\nGuardado: ejercicio06_filtrado_ordenado.csv")

if __name__ == "__main__":
    main()

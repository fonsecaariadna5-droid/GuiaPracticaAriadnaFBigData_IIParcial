# ejercicio08
import pandas as pd

def main():
    df = pd.read_csv("ventas.csv")
    df['Total'] = pd.to_numeric(df['Total'], errors='coerce').fillna(0)

    # parámetros: puedes cambiarlos aquí o adaptarlos para input()
    total_min = float(input("Total mínimo (ej: 50): ") or 0)
    total_max = float(input("Total máximo (ej: 1000): ") or 1e12)
    producto = input("Producto a filtrar (dejar vacío para omitir): ").strip()
    clientes_str = input("Lista de clientes separados por comas (dejar vacío para omitir): ").strip()
    clientes = [c.strip() for c in clientes_str.split(",")] if clientes_str else []

    mask = (df['Total'] >= total_min) & (df['Total'] <= total_max)
    if producto:
        mask &= df['Producto'].astype(str).str.lower() == producto.lower()
    if clientes:
        mask &= df['Cliente'].astype(str).isin(clientes)

    resultados = df[mask]
    print(f"Registros resultantes: {len(resultados)}")
    resultados.to_csv("ejercicio08_filtrado_multiple.csv", index=False)
    print("Guardado: ejercicio08_filtrado_multiple.csv")

if __name__ == "__main__":
    main()

# ejercicio07
import pandas as pd

def main():
    df = pd.read_csv("ventas.csv", dtype=str)
    if 'Cliente' not in df.columns:
        print("No encontré la columna 'Cliente'.")
        return

    text = input("Ingresa texto a buscar en Cliente (insensible a mayúsc/minúsc): ").strip()
    if not text:
        print("No ingresaste texto. Saliendo.")
        return

    mask = df['Cliente'].str.contains(text, case=False, na=False)
    resultados = df[mask]
    print(f"Resultados encontrados: {len(resultados)}\n")
    print(resultados.head(50))
    resultados.to_csv("ejercicio07_busqueda_cliente.csv", index=False)
    print("\nGuardado: ejercicio07_busqueda_cliente.csv")

if __name__ == "__main__":
    main()

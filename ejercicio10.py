# ejercicio10
import pandas as pd

def main():
    chunk_size = int(input("Tamaño de chunk (ej: 1000): ") or 1000)
    total_global = 0.0
    i = 0
    for chunk in pd.read_csv("ventas.csv", chunksize=chunk_size):
        i += 1
        chunk['Total'] = pd.to_numeric(chunk['Total'], errors='coerce').fillna(0)
        subtotal = chunk['Total'].sum()
        print(f"Chunk {i}: subtotal = {subtotal}")
        total_global += float(subtotal)
    print(f"\nTotal global acumulado: {round(total_global,2)}")

if __name__ == "__main__":
    main()

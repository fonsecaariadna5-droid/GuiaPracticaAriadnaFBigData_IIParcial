# ejercicio14
import pandas as pd
import time

def method_normal(path="ventas.csv"):
    t0 = time.perf_counter()
    df = pd.read_csv(path)
    df['Total'] = pd.to_numeric(df['Total'], errors='coerce').fillna(0)
    total = df['Total'].sum()
    t1 = time.perf_counter()
    return total, t1 - t0

def method_chunks(path="ventas.csv", chunk_size=10000):
    t0 = time.perf_counter()
    total = 0.0
    for chunk in pd.read_csv(path, chunksize=chunk_size):
        chunk['Total'] = pd.to_numeric(chunk['Total'], errors='coerce').fillna(0)
        total += chunk['Total'].sum()
    t1 = time.perf_counter()
    return total, t1 - t0

def main():
    path = "ventas.csv"
    print("Ejecutando método normal...")
    total_normal, time_normal = method_normal(path)
    print(f"Total normal: {total_normal} — tiempo: {time_normal:.4f} s")

    print("\nEjecutando método por chunks...")
    chunk_size = int(input("Chunk size para benchmark (ej: 10000): ") or 10000)
    total_chunk, time_chunk = method_chunks(path, chunk_size)
    print(f"Total chunks: {total_chunk} — tiempo: {time_chunk:.4f} s")

    print("\nResumen comparativo:")
    print(f"Método normal: {time_normal:.4f} s")
    print(f"Método chunks: {time_chunk:.4f} s")
    if time_chunk < time_normal:
        print("Chunks fue más rápido.")
    else:
        print("Lectura completa fue más rápido (o similar).")

if __name__ == "__main__":
    main()

# ejercicio11
import pandas as pd
from collections import defaultdict

def main():
    chunk_size = int(input("Tamaño de chunk (ej: 1000): ") or 1000)
    agg = defaultdict(float)  # producto -> suma total

    for chunk in pd.read_csv("ventas.csv", chunksize=chunk_size):
        chunk['Total'] = pd.to_numeric(chunk['Total'], errors='coerce').fillna(0)
        g = chunk.groupby('Producto')['Total'].sum()
        for producto, total in g.items():
            agg[producto] += float(total)

    # convertir a DataFrame para mostrar / guardar
    df_res = pd.DataFrame(list(agg.items()), columns=['Producto','Total_Sum']).sort_values('Total_Sum', ascending=False)
    print(df_res.head(20))
    df_res.to_csv("ejercicio11_agrupado_producto.csv", index=False)
    print("Guardado: ejercicio11_agrupado_producto.csv")

if __name__ == "__main__":
    main()

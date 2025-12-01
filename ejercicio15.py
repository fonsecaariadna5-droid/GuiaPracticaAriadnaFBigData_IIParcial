# ejercicio15.py
import pandas as pd
import re
import os

def sanitize_filename(name):
    # eliminar caracteres inválidos para Windows: <>:"/\\|?* y recortar espacios
    if pd.isna(name):
        name = "NA"
    name = str(name)
    name = re.sub(r'[<>:"/\\\\|?*]', '_', name)
    name = name.strip()
    # limitar longitud a 100 caracteres
    return name[:100] if len(name) > 100 else name

def main():
    df = pd.read_csv("ventas.csv")
    df['Total'] = pd.to_numeric(df['Total'], errors='coerce').fillna(0)

    # Resumen por producto
    resumen_producto = df.groupby('Producto')['Total'].agg(['count','sum','mean']).reset_index().rename(columns={'count':'Cantidad_Registros','sum':'Total_Sum','mean':'Total_Mean'})
    resumen_producto.to_csv("ejercicio15_resumen_por_producto.csv", index=False)
    print("Guardado: ejercicio15_resumen_por_producto.csv")

    # Resumen por cliente
    resumen_cliente = df.groupby('Cliente')['Total'].agg(['count','sum','mean']).reset_index().rename(columns={'count':'Cantidad_Registros','sum':'Total_Sum','mean':'Total_Mean'})
    resumen_cliente.to_csv("ejercicio15_resumen_por_cliente.csv", index=False)
    print("Guardado: ejercicio15_resumen_por_cliente.csv")

    # Exportar archivos particionados por producto
    out_dir = "ejercicio15_productos_particionados"
    os.makedirs(out_dir, exist_ok=True)
    productos = df['Producto'].dropna().unique()
    for p in productos:
        fname = sanitize_filename(p)
        df_p = df[df['Producto'] == p]
        out_path = os.path.join(out_dir, f"{fname}.csv")
        df_p.to_csv(out_path, index=False)
    print(f"Exportados {len(productos)} archivos en carpeta: {out_dir}")

if __name__ == "__main__":
    main()

import pandas as pd

archivo = "datos.xlsx"  # crea un Excel simple

df = pd.read_excel(archivo)

print("Datos:")
print(df)

print("\nPromedio:")
print(df.mean())

print("\nMáximo:")
print(df.max())

print("\nMínimo:")
print(df.min())

print("\nCantidad de registros:")
print(len(df))

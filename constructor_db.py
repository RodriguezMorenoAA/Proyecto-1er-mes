import pandas as pd
import sqlite3

print("Voy a leer el archivo.csv...")
df = pd.read_csv("datos_crudos.csv")

df = df[["pl_name", "pl_bmasse", "pl_rade"]]
df.columns = ["nombre", "masa", "radio"]

df = df.dropna(subset=["masa", "radio"])
df = df[(df["masa"] > 0) & (df["radio"] > 0)]

print(f"Datos limpios: {len(df)} planetas")

conn = sqlite3.connect("datos_mision.db")

df.to_sql("planetas", conn, if_exists="replace", index=False)

conn.close()

print("Base de datos creada correctamente.")

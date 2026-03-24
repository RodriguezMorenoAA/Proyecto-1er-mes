import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

print("Cargando datos desde el SQLite anterior...")

conn = sqlite3.connect("datos_mision.db")

query = "SELECT nombre, masa, radio FROM planetas"
df = pd.read_sql_query(query, conn)

conn.close()

df["densidad"] = df["masa"] / (df["radio"]**3)

df["tipo"] = np.where(df["radio"] < 1.8, "rocoso", "gaseoso") #El dato de 1.8 lo gogleé jeje

print("Generando gráfica...")

plt.figure()

for tipo in ["rocoso", "gaseoso"]:
    subset = df[df["tipo"] == tipo]
    plt.scatter(
        subset["radio"],
        subset["masa"],
	s=15,
        label=tipo,
	alpha=0.6
    )

plt.xscale("log")
plt.yscale("log")

plt.xlabel("Radio (R⊕)") #Ese simbolo terrestre lo gogleé jeje
plt.ylabel("Masa (M⊕)")
plt.title("Relación Masa-Radio de Exoplanetas")
plt.grid()
plt.legend()
plt.savefig("resultado.png", dpi=300) 
# Esto no me acordaba y se lo pedí a gemini (hace mucho no guardo imagenes en python)
# (Suelo tomar pantallazos) y la instrucción a la IA fue literalmente:
# "Estoy haciendo un codigo de python y necesito guardar mi imagen en formato png y no se hacerlo"

print("Gráfica generada: resultado.png")

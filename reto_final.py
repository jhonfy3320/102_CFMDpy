import matplotlib.pyplot as plt
import pandas as pd

# Cargar los datos desde el archivo CSV
data = pd.read_csv("world_population.csv")

# Extraer las columnas de país y población
paises = data["Country"]
poblacion = data["Population"]

# Crear una figura y ejes para el gráfico
fig, ax = plt.subplots()

# Graficar los datos de población
ax.barh(paises, poblacion, color='skyblue')

# Personalizar el gráfico
ax.set_xlabel("Población")
ax.set_ylabel("País")
ax.set_title("Población Mundial por País")
ax.invert_yaxis()  # Invertir el eje y para que los países se muestren en orden descendente

# Mostrar el gráfico
plt.tight_layout()
plt.show()

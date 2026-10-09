import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# leo el csv que creamos
datos = pd.read_csv("datos_estaciones.csv")

# me quedo solo con los números (el nombre no sirve para agrupar)
X = datos[["pasajeros_dia", "espera_min", "retrasos_mes"]]

# pongo todo en la misma escala, si no los pasajeros pesan mucho más
X_escalado = StandardScaler().fit_transform(X)

# k-means con 3 grupos
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
datos["grupo"] = kmeans.fit_predict(X_escalado)

# qué tan bien quedaron separados los grupos (entre más cerca de 1, mejor)
print("Silhouette:", round(silhouette_score(X_escalado, datos["grupo"]), 2))

# promedio de cada grupo para entender cómo es cada uno
print("\nPromedio por grupo:")
print(datos.groupby("grupo")[["pasajeros_dia", "espera_min", "retrasos_mes"]].mean().round(1))

# qué estaciones quedaron en cada grupo
print("\nEstaciones por grupo:")
for g in sorted(datos["grupo"].unique()):
    print("Grupo", g, ":", list(datos[datos["grupo"] == g]["estacion"]))

# gráfica para el video
plt.scatter(datos["pasajeros_dia"], datos["retrasos_mes"], c=datos["grupo"])
plt.xlabel("Pasajeros por día")
plt.ylabel("Retrasos al mes")
plt.title("Grupos de estaciones de TransMilenio")
plt.show()
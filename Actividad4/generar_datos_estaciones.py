import random
import csv

random.seed(7)  # para que siempre salgan los mismos datos

estaciones = ["Portal Norte", "Calle 100", "Av. Chile", "Av. Jiménez", "Portal Sur",
              "Portal Américas", "Portal 80", "Portal Tunal", "Universidades",
              "Museo del Oro", "Calle 76", "Ricaurte", "Banderas", "Av. Primero de Mayo",
              "Marly", "Calle 45", "Alcalá", "Prado", "Toberín", "Terminal"]

filas = []
for nombre in estaciones:
    # reparto cada estación en un tipo para que los datos tengan sentido
    tipo = random.choice(["muy_concurrida", "normal", "tranquila"])

    if tipo == "muy_concurrida":
        pasajeros = random.randint(8000, 12000)
        espera = random.uniform(6, 10)
        retrasos = random.randint(15, 30)
    elif tipo == "normal":
        pasajeros = random.randint(4000, 7000)
        espera = random.uniform(3, 6)
        retrasos = random.randint(5, 15)
    else:
        pasajeros = random.randint(500, 3000)
        espera = random.uniform(1, 3)
        retrasos = random.randint(0, 6)

    filas.append([nombre, pasajeros, round(espera, 1), retrasos])

# guardo todo en un csv
with open("datos_estaciones.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["estacion", "pasajeros_dia", "espera_min", "retrasos_mes"])
    w.writerows(filas)

print("Listo, dataset creado")
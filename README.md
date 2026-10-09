# Agrupamiento de estaciones de TransMilenio

Última actividad del curso de Inteligencia Artificial (IBERO).
Usamos K-means (aprendizaje no supervisado) para agrupar estaciones
de TransMilenio según pasajeros, tiempo de espera y retrasos.

## Integrantes
- Lizeth Vanessa Millán Nieto
- Mado Alexandra Millán Nieto


## Archivos
- `generar_datos_estaciones.py`: crea el dataset de muestra (20 estaciones simuladas)
- `datos_estaciones.csv`: los datos generados
- `agrupamiento.py`: aplica K-means y muestra los resultados
- `Documento_Actividad6.docx`: descripción de los datos y pruebas realizadas

## Cómo ejecutarlo
1. Instalar las librerías: `pip install pandas scikit-learn matplotlib`
2. Crear los datos: `python generar_datos_estaciones.py`
3. Correr el modelo: `python agrupamiento.py`

## Resultado
K-means formó 3 grupos de estaciones (tranquilas, normales y muy
concurridas) con un Silhouette de 0.59.

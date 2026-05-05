# retail-sales-analysis
Análisis y Predicción de Ventas en una Tienda de Retail (Core)
# Retail Sales Analysis

Análisis y Predicción de Ventas en una Tienda de Retail (Core)



## Descripción

En este proyecto se realiza un análisis básico de un dataset de ventas de retail utilizando NumPy. 
Se exploran los datos, se calculan métricas clave y se analizan las ventas por categoría de producto.


## Dataset

Para el desarrollo se utiliza el dataset Retail Sales Dataset (2023-2024), que contiene información sobre los siguientes aspectos distribuidos en 9 columnas.

- Transaction ID 
- Date 
- Customer ID 
- Gender 
- Age 
- Product Category 
- Quantity 
- Price per Unit 
- Total Amount 

## Carga de Datos

Se realizó una carga inicial con NumPy según el enunciado:

datos = np.genfromtxt(ruta_archivo, delimiter=',', skip_header=1)

Sin embargo, algunas columnas aparecían como nan debido a la presencia de datos de tipo texto, ya que NumPy intentó interpretarlos como números.

Considerando eso realicé lo siguiente: 
datos = np.genfromtxt(ruta_archivo, delimiter=',', skip_header=1, dtype=str).

Se utilizó np.unique para identificar las categorías distintas dentro de la columna "Product Category". (Este recurso lo utilicé en base a lo revisado en clase a partir de una consulta realizada por la compañera Helen al profesor Jesús).



## Análisis Realizado

1. Total,de ventas por categoría

Se utilizó np.unique para obtener las categorías y luego se sumaron las ventas correspondientes.

Resultados:

- Beauty: $143,515 
- Clothing: $155,580 
- Electronics: $156,905 


2. Promedio de ventas por categoría

Se calculó dividiendo el total de ventas por la cantidad de registros en cada categoría.

Resultados:

- Beauty: $467.48 
- Clothing: $443.25 
- Electronics: $458.79 


3. Categorías con mayor y menor venta

Se utilizaron estas funciones de NumPy (me basé en el Core anterior a este:

np.argmax()
np.argmin()

Resultados:

- Mayor venta: Electronics 
- Menor venta: Beauty 

---

4. Filtrado de datos

Se filtraron registros por categoría, por ejemplo:

[fila for fila in datos if fila[5] == 'Beauty']



5. Transformaciones

Se realizaron operaciones como:

- Conversión de datos a tipo numérico usando astype(float) 



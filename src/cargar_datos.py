import numpy as np

# Cargar datos
datos = np.genfromtxt(
    '../data/retail_sales_dataset.csv',
    delimiter=',',
    skip_header=1,
    dtype=None,
    encoding='utf-8'
)

print("Dimensiones:", datos.shape)
print("\nPrimeras filas:")
print(datos[:5])

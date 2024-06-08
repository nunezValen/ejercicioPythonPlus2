import pandas as pd

file_route = "area_protegida.csv"

def calc_value(df):
    # Utilizo : para seleccionar todas las filas y el 13 indica la columna.
    # .mean Calcula el promedio
    value = df.iloc[:, 13].mean() 
    return value

def my_function(df, value, *args):
    # .iloc Metodo para seleccionar datos por posición. Igual que antes : para todas las filas y 8 para la columna.
    # .isin Metodo para ver si el dato esta contenido en una lista u otro objeto iterable.
    # Luego hago iloc con 13 para filtrar aquellos menores al promedio y que cumplen con lo anterior.
    sub_data = df[(df.iloc[:, 8].isin(args)) & (df.iloc[:, 13] < value)]
    return sub_data

# Leer el archivo CSV usando pandas
df = pd.read_csv(file_route, encoding="utf-8")

# Calcular el valor promedio de las areas
value_data = calc_value(df)

# Filtrar los datos según tap y el promedio
result1 = my_function(df, value_data, 1, 2)
result2 = my_function(df, value_data, 3)

# Mostrar los resultados
print(len(result1))
print(f"\n****\n{len(result2)}")

# Ver tipo dataframe
print(type(df))

# Ver tipo series
#print(type(result1))

# Ver todos los tipos de las columnas del dataframe
print(df.dtypes)

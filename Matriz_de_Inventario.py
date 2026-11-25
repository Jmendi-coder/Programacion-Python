# Johann Alberto Mendivil Palencia
# Grupo: 213022_101
# Fundamentos de la programación: Fase 5 - Evaluación Final POA
# Código Fuente: Autoría Propia
# Problema 3: Matriz de Inventario

# Creamos una matriz de inventario con los siguientes datos: código, producto, stock actual y stock mínimo
# Cada fila representa un articulo y contiene cuatro datos:
# Posición [0]: Código del artículo
# Posición [1]: Nombre del artículo
# Posición [2]: Stock actual
# Posición [3]: Stock mínimo requerido
inventario = [
    [101, "Arroz", 8, 20],
    [102, "Panela", 25, 15],
    [103, "Azúcar", 5, 12],
    [104, "Aceite", 10, 10],
    [105, "Café", 3, 18]
]


# Función para calcular la cantidad que se debe pedir
# Esta función recibe el stock  actual y el stock mínimo, compara los valores y devuelve la cantidad que se debe pedir
def calcular_reabastecimiento(stock_actual, stock_minimo):
    # Se crea la condición para determinar si el stock actual es menor al stock mínimo, en caso de ser así se calcula la 
    # cantidad a pedir, de lo contrario se devuelve 0
    if stock_actual < stock_minimo:
        cantidad_pedir = stock_minimo - stock_actual
    else:
        cantidad_pedir = 0

    return cantidad_pedir


# Creamos un ciclo para recorrer la matriz y mostrar los resultados permitiendo ver el producto y la cantidad que se debe pedir
print("*------ INFORME DE REABASTECIMIENTO ------*")

for articulo in inventario:

    codigo = articulo[0]
    producto = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad = calcular_reabastecimiento(stock_actual, stock_minimo)

    print(producto, "-> Cantidad a solicitar:", cantidad)

print("   *------ FIN DEL INFORME ------*  ")

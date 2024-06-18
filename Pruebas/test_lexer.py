# pruebas/test_streaks_lexer.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from streaks_lexer import lexer

def test_lexer():
    data = '''
    // Declaración del modelo con la matriz delta 
model myModel = (0.5, [1, 2], [3, 4], [
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
]);

// Operaciones de información del modelo
print("Total de datos del modelo:");
myModel.total_datos();

print("Total de datos del bloque 0:");
myModel.total_datos_bloque(0);

print("Total de datos del tratamiento 1:");
myModel.total_datos_tratamiento(1);

print("Datos del modelo:");// Declaración del modelo con la matriz delta
model myModel = (0.5, [1, 2], [3, 4], [
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
]);

// Imprimir el total de datos en el modelo
print("Total de datos en el modelo:");
myModel.total_datos();

// Imprimir el total de datos en el bloque 0
print("Total de datos en el bloque 0:");
myModel.total_datos_bloque(0);

// Imprimir el total de datos en el tratamiento 1
print("Total de datos en el tratamiento 1:");
myModel.total_datos_tratamiento(1);

// Imprimir la matriz de datos del modelo
print("Matriz de datos del modelo:");
myModel.datos_modelo();

// Imprimir los datos del bloque 0
print("Datos del bloque 0:");
myModel.datos_bloque(0);

// Imprimir los datos del tratamiento 1
print("Datos del tratamiento 1:");
myModel.datos_tratamiento(1);

// Definición de la matriz R para pruebas de rachas
var R = [
    [[1, 1], [2, 2]],
    [[3, 3], [4, 4]]
];

// Imprimir el total de rachas en R
print("Total de rachas en R:");
myModel.total_runs(R);

// Imprimir el promedio de rachas por celda en R
print("Promedio de rachas por celda en R:");
myModel.average_runs_per_cell(R);

// Imprimir el total de rachas por bloque en R
print("Total de rachas por bloque en R:");
myModel.total_runs_block(R);

// Imprimir el total de rachas por tratamiento en R
print("Total de rachas por tratamiento en R:");
myModel.total_runs_treatment(R);

// Imprimir el promedio de rachas por bloque en R
print("Promedio de rachas por bloque en R:");
myModel.average_runs_block(R);

// Imprimir el promedio de rachas por tratamiento en R
print("Promedio de rachas por tratamiento en R:");
myModel.average_runs_treatment(R);

// Imprimir el total de rachas en todo el modelo R
print("Total de rachas en todo el modelo R:");
myModel.total_runs_model(R);

// Imprimir el promedio de rachas en todo el modelo R
print("Promedio de rachas en todo el modelo R:");
myModel.average_runs_model(R);

// Definición de una cadena para pruebas de la función contadora y número de rachas
var cadena = "aaaabbbaaa";

// Imprimir la función contadora para la cadena
print("Función contadora para la cadena:");
myModel.funcion_contadora(cadena);

// Imprimir el número de rachas en la cadena
print("Número de rachas en la cadena:");
myModel.numero_de_rachas(cadena);

// Imprimir la suma de rachas en la celda (0, 1)
print("Suma de rachas en la celda (0, 1):");
myModel.suma_de_rachas_celda(0, 1);

// Imprimir el promedio de rachas en la celda (0, 1)
print("Promedio de rachas en la celda (0, 1):");
myModel.promedio_de_rachas_celda(0, 1);

myModel.datos_modelo();

print("Datos del bloque 1:");
myModel.datos_bloque(1);

print("Datos del tratamiento 0:");
myModel.datos_tratamiento(0);

// Definición de una nueva matriz R para realizar más operaciones
var R = [
    [
        [9, 10],
        [11, 12]
    ],
    [
        [13, 14],
        [15, 16]
    ]
];

// Operaciones con la nueva matriz R
print("Total de runs en la nueva matriz R:");
myModel.total_runs(R);

print("Promedio de runs por celda en la nueva matriz R:");
myModel.average_runs_per_cell(R);

print("Total de runs por bloque en la nueva matriz R:");
myModel.total_runs_block(R);

print("Total de runs por tratamiento en la nueva matriz R:");
myModel.total_runs_treatment(R);

print("Promedio de runs por bloque en la nueva matriz R:");
myModel.average_runs_block(R);

print("Promedio de runs por tratamiento en la nueva matriz R:");
myModel.average_runs_treatment(R);

print("Total de runs en el modelo con la nueva matriz R:");
myModel.total_runs_model(R);

print("Promedio de runs en el modelo con la nueva matriz R:");
myModel.average_runs_model(R);

    '''

    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

if __name__ == "__main__":
    test_lexer()

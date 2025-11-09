# multilang-python: es
"""
Ejemplo de procesamiento de datos en español
Procesa una lista de estudiantes y calcula estadísticas
"""

funcion crear_estudiante(nombre, edad, notas):
    """Crea un diccionario representando un estudiante."""
    retornar {
        "nombre": nombre,
        "edad": edad,
        "notas": notas,
        "promedio": calcular_promedio(notas)
    }

funcion calcular_promedio(notas):
    """Calcula el promedio de una lista de notas."""
    si longitud(notas) == 0:
        retornar 0
    retornar suma(notas) / longitud(notas)

funcion filtrar_aprobados(estudiantes, umbral=10):
    """Filtra los estudiantes que aprobaron (promedio >= umbral)."""
    aprobados = []
    para estudiante en estudiantes:
        si estudiante["promedio"] >= umbral:
            aprobados.append(estudiante)
    retornar aprobados

funcion mostrar_estadisticas(estudiantes):
    """Muestra las estadísticas de la clase."""
    mostrar("\n=== Estadísticas de la clase ===")
    mostrar(f"Número de estudiantes: {longitud(estudiantes)}")

    si longitud(estudiantes) == 0:
        mostrar("¡No hay estudiantes!")
        retornar

    # Calcular los promedios
    promedios = [e["promedio"] para e en estudiantes]

    mostrar(f"Promedio de clase: {calcular_promedio(promedios):.2f}")
    mostrar(f"Mejor promedio: {maximo(promedios):.2f}")
    mostrar(f"Promedio más bajo: {minimo(promedios):.2f}")

    # Mostrar los estudiantes
    mostrar("\n=== Lista de estudiantes ===")
    para i, estudiante en enumerar(estudiantes, 1):
        mostrar(f"{i}. {estudiante['nombre']} (edad: {estudiante['edad']}) - Promedio: {estudiante['promedio']:.2f}")

funcion principal():
    """Programa principal."""
    # Crear ejemplos de estudiantes
    estudiantes = [
        crear_estudiante("Ana García", 20, [15, 17, 16, 18]),
        crear_estudiante("Carlos López", 19, [12, 14, 13, 15]),
        crear_estudiante("Diana Rodríguez", 21, [18, 19, 17, 20]),
        crear_estudiante("Eduardo Martínez", 20, [8, 9, 7, 10]),
        crear_estudiante("Fernanda Torres", 19, [16, 15, 17, 16])
    ]

    # Mostrar todas las estadísticas
    mostrar("=== Todos los estudiantes ===")
    mostrar_estadisticas(estudiantes)

    # Filtrar los estudiantes que aprobaron
    aprobados = filtrar_aprobados(estudiantes, 12)

    mostrar("\n=== Estudiantes que aprobaron (promedio >= 12) ===")
    mostrar_estadisticas(aprobados)

    # Ordenar por promedio (descendente)
    estudiantes_ordenados = ordenar(estudiantes, key=lambda e: e["promedio"], reverse=verdadero)

    mostrar("\n=== Clasificación por promedio ===")
    para rango, estudiante en enumerar(estudiantes_ordenados, 1):
        mostrar(f"{rango}. {estudiante['nombre']}: {estudiante['promedio']:.2f}")

# Punto de entrada
si __name__ == "__main__":
    principal()

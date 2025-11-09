# multilang-python: es
"""
Calculadora simple en español
Soporta las operaciones básicas: +, -, *, /
"""

funcion suma(a, b):
    """Suma dos números."""
    retornar a + b

funcion resta(a, b):
    """Resta b de a."""
    retornar a - b

funcion multiplicacion(a, b):
    """Multiplica dos números."""
    retornar a * b

funcion division(a, b):
    """Divide a por b."""
    si b == 0:
        retornar "Error: División por cero!"
    retornar a / b

funcion calcular(numero1, operacion, numero2):
    """Realiza el cálculo según la operación elegida."""
    si operacion == "+":
        retornar suma(numero1, numero2)
    si_no operacion == "-":
        retornar resta(numero1, numero2)
    si_no operacion == "*":
        retornar multiplicacion(numero1, numero2)
    si_no operacion == "/":
        retornar division(numero1, numero2)
    sino:
        retornar "Operación inválida!"

funcion principal():
    """Programa principal de la calculadora."""
    mostrar("=== Calculadora Simple ===")
    mostrar("Operaciones disponibles: +, -, *, /")
    mostrar()

    intentar:
        # Pedir el primer número
        num1 = flotante(entrada("Ingrese el primer número: "))

        # Pedir la operación
        op = entrada("Ingrese la operación (+, -, *, /): ")

        # Pedir el segundo número
        num2 = flotante(entrada("Ingrese el segundo número: "))

        # Calcular y mostrar el resultado
        resultado = calcular(num1, op, num2)
        mostrar(f"\nResultado: {num1} {op} {num2} = {resultado}")

    excepto ValueError:
        mostrar("Error: Por favor ingrese números válidos!")
    excepto Exception como e:
        mostrar(f"Error inesperado: {e}")

# Punto de entrada
si __name__ == "__main__":
    principal()

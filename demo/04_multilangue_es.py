# multilang-python: es
"""
Démo 4A: Exemple en Espagnol
Temps: 1 minute
Montre: Support multi-langues
"""

funcion saludar(nombre):
    """Saluda en español."""
    mostrar(f"¡Hola, {nombre}!")
    mostrar("¡Bienvenido a multilang-python! 🇪🇸")

# Saludar varios usuarios
mostrar("═" * 50)
mostrar("     🌮 PYTHON EN ESPAÑOL 🌮")
mostrar("═" * 50)
mostrar()

nombres = ["Carlos", "María", "José", "Ana"]

para nombre en nombres:
    saludar(nombre)
    mostrar()

mostrar("✅ ¡7 idiomas soportados!")
mostrar("   FR, ES, DE, PT, IT, AR, ZH")

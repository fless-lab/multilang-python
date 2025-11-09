# multilang-python: de
"""
Démo 4B: Exemple en Allemand
Temps: 1 minute
Montre: Support multi-langues
"""

funktion gruessen(name):
    """Grüßt auf Deutsch."""
    drucken(f"Hallo, {name}! 🇩🇪")
    drucken("Willkommen bei multilang-python!")

# Demo
drucken("═" * 50)
drucken("      🥨 PYTHON AUF DEUTSCH 🥨")
drucken("═" * 50)
drucken()

fuer i in bereich(1, 4):
    gruessen(f"Benutzer {i}")
    drucken()

drucken("✅ Funktioniert perfekt!")

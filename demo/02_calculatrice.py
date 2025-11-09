# multilang-python: fr
"""
Démo 2: Calculatrice Interactive
Temps: 2-3 minutes
Montre: structures de contrôle, fonctions
"""

fonction calculer(a, b, operation):
    """Effectue une opération mathématique."""
    si operation == "+":
        retourner a + b
    sinon_si operation == "-":
        retourner a - b
    sinon_si operation == "*":
        retourner a * b
    sinon_si operation == "/":
        si b != 0:
            retourner a / b
        sinon:
            retourner "❌ Erreur: Division par zéro!"
    sinon:
        retourner "❌ Opération invalide!"

# Démonstration
afficher("═" * 50)
afficher("         🧮 CALCULATRICE EN FRANÇAIS 🧮")
afficher("═" * 50)
afficher()

operations = [
    (10, 5, "+"),
    (10, 5, "-"),
    (10, 5, "*"),
    (10, 5, "/"),
    (10, 0, "/"),
]

pour a, b, op dans operations:
    resultat = calculer(a, b, op)
    afficher(f"  {a} {op} {b} = {resultat}")

afficher()
afficher("✅ Si/Sinon, Fonctions, Boucles... tout en français!")

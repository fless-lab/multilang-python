# multilang-python: fr
"""
Calculatrice simple en français
Supporte les opérations de base: +, -, *, /
"""

fonction addition(a, b):
    """Additionne deux nombres."""
    retourner a + b

fonction soustraction(a, b):
    """Soustrait b de a."""
    retourner a - b

fonction multiplication(a, b):
    """Multiplie deux nombres."""
    retourner a * b

fonction division(a, b):
    """Divise a par b."""
    si b == 0:
        retourner "Erreur: Division par zéro!"
    retourner a / b

fonction calculer(nombre1, operation, nombre2):
    """Effectue le calcul selon l'opération choisie."""
    si operation == "+":
        retourner addition(nombre1, nombre2)
    sinon_si operation == "-":
        retourner soustraction(nombre1, nombre2)
    sinon_si operation == "*":
        retourner multiplication(nombre1, nombre2)
    sinon_si operation == "/":
        retourner division(nombre1, nombre2)
    sinon:
        retourner "Opération invalide!"

fonction principale():
    """Programme principal de la calculatrice."""
    afficher("=== Calculatrice Simple ===")
    afficher("Opérations disponibles: +, -, *, /")
    afficher()

    essayer:
        # Demander le premier nombre
        num1 = flottant(saisir("Entrez le premier nombre: "))

        # Demander l'opération
        op = saisir("Entrez l'opération (+, -, *, /): ")

        # Demander le deuxième nombre
        num2 = flottant(saisir("Entrez le deuxième nombre: "))

        # Calculer et afficher le résultat
        resultat = calculer(num1, op, num2)
        afficher(f"\nRésultat: {num1} {op} {num2} = {resultat}")

    sauf ValueError:
        afficher("Erreur: Veuillez entrer des nombres valides!")
    sauf Exception comme e:
        afficher(f"Erreur inattendue: {e}")

# Point d'entrée
si __name__ == "__main__":
    principale()

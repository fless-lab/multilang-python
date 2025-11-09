# multilang-python: fr
"""
Exemple simple : Salutations en français
"""

fonction saluer(nom):
    """Affiche un message de salutation."""
    afficher(f"Bonjour, {nom}!")
    afficher("Bienvenue dans multilang-python!")

fonction principale():
    """Fonction principale du programme."""
    # Demander le nom de l'utilisateur
    nom = saisir("Quel est votre nom? ")

    # Saluer l'utilisateur
    saluer(nom)

    # Afficher quelques informations
    afficher("\nCe programme est écrit en Python...")
    afficher("...mais avec des mots-clés français!")

# Point d'entrée du programme
si __name__ == "__main__":
    principale()

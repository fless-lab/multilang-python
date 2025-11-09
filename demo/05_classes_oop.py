# multilang-python: fr
"""
Démo 5: Programmation Orientée Objet
Temps: 3 minutes
Montre: Classes, héritage, méthodes
"""

classe Animal:
    """Classe de base pour les animaux."""

    fonction __init__(soi, nom, age):
        soi.nom = nom
        soi.age = age

    fonction presenter(soi):
        afficher(f"Je suis {soi.nom}, j'ai {soi.age} ans")

    fonction faire_bruit(soi):
        afficher("*bruit d'animal*")


classe Chien(Animal):
    """Un chien est un animal qui aboie."""

    fonction __init__(soi, nom, age, race):
        super().__init__(nom, age)
        soi.race = race

    fonction presenter(soi):
        afficher(f"🐕 Je suis {soi.nom}, un {soi.race} de {soi.age} ans")

    fonction faire_bruit(soi):
        afficher("Wouf! Wouf! 🦴")


classe Chat(Animal):
    """Un chat est un animal qui miaule."""

    fonction __init__(soi, nom, age, couleur):
        super().__init__(nom, age)
        soi.couleur = couleur

    fonction presenter(soi):
        afficher(f"🐱 Je suis {soi.nom}, un chat {soi.couleur} de {soi.age} ans")

    fonction faire_bruit(soi):
        afficher("Miaou! Miaou! 🐟")


# Démonstration
afficher("═" * 60)
afficher("         🐾 PROGRAMMATION ORIENTÉE OBJET 🐾")
afficher("═" * 60)
afficher()

# Créer des animaux
rex = Chien("Rex", 3, "Labrador")
felix = Chat("Félix", 2, "noir")

# Les présenter
animaux = [rex, felix]

pour animal dans animaux:
    animal.presenter()
    animal.faire_bruit()
    afficher()

afficher("✅ Classes, Héritage, Méthodes... POO complète!")

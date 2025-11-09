# multilang-python: fr
"""
Démo 3: Analyse de Données
Temps: 3 minutes
Montre: fonctions avancées, lambda, dictionnaires
"""

fonction analyser(nombres):
    """Analyse statistique d'une liste de nombres."""
    # Filtrer pairs et impairs
    pairs = liste(filtrer(lambda x: x % 2 == 0, nombres))
    impairs = liste(filtrer(lambda x: x % 2 != 0, nombres))

    # Calculer statistiques
    total = somme(nombres)
    moyenne = total / longueur(nombres)

    retourner {
        "total": total,
        "moyenne": arrondir(moyenne, 2),
        "pairs": pairs,
        "impairs": impairs,
        "max": maximum(nombres),
        "min": minimum(nombres),
        "compte": longueur(nombres)
    }

# Données de démonstration
afficher("═" * 60)
afficher("           📊 ANALYSE DE DONNÉES EN FRANÇAIS 📊")
afficher("═" * 60)
afficher()

nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30]
afficher(f"📋 Données: {nombres}")
afficher()

resultats = analyser(nombres)

afficher("📈 STATISTIQUES:")
afficher(f"  • Nombre d'éléments : {resultats['compte']}")
afficher(f"  • Total            : {resultats['total']}")
afficher(f"  • Moyenne          : {resultats['moyenne']}")
afficher(f"  • Maximum          : {resultats['max']}")
afficher(f"  • Minimum          : {resultats['min']}")
afficher()

afficher("🔢 RÉPARTITION:")
afficher(f"  • Nombres pairs    : {resultats['pairs']}")
afficher(f"  • Nombres impairs  : {resultats['impairs']}")
afficher()

afficher("✅ Lambda, Filtrer, Somme, Maximum... tout fonctionne!")

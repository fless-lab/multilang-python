# multilang-python: fr
"""
Exemple de traitement de données en français
Traite une liste d'étudiants et calcule des statistiques
"""

fonction creer_etudiant(nom, age, notes):
    """Crée un dictionnaire représentant un étudiant."""
    retourner {
        "nom": nom,
        "age": age,
        "notes": notes,
        "moyenne": calculer_moyenne(notes)
    }

fonction calculer_moyenne(notes):
    """Calcule la moyenne d'une liste de notes."""
    si longueur(notes) == 0:
        retourner 0
    retourner somme(notes) / longueur(notes)

fonction filtrer_reussis(etudiants, seuil=10):
    """Filtre les étudiants ayant réussi (moyenne >= seuil)."""
    reussis = []
    pour etudiant dans etudiants:
        si etudiant["moyenne"] >= seuil:
            reussis.append(etudiant)
    retourner reussis

fonction afficher_statistiques(etudiants):
    """Affiche les statistiques de la classe."""
    afficher("\n=== Statistiques de la classe ===")
    afficher(f"Nombre d'étudiants: {longueur(etudiants)}")

    si longueur(etudiants) == 0:
        afficher("Aucun étudiant!")
        retourner

    # Calculer les moyennes
    moyennes = [e["moyenne"] pour e dans etudiants]

    afficher(f"Moyenne de classe: {calculer_moyenne(moyennes):.2f}")
    afficher(f"Meilleure moyenne: {maximum(moyennes):.2f}")
    afficher(f"Plus faible moyenne: {minimum(moyennes):.2f}")

    # Afficher les étudiants
    afficher("\n=== Liste des étudiants ===")
    pour i, etudiant dans enumerer(etudiants, 1):
        afficher(f"{i}. {etudiant['nom']} (âge: {etudiant['age']}) - Moyenne: {etudiant['moyenne']:.2f}")

fonction principale():
    """Programme principal."""
    # Créer des exemples d'étudiants
    etudiants = [
        creer_etudiant("Alice Dupont", 20, [15, 17, 16, 18]),
        creer_etudiant("Bob Martin", 19, [12, 14, 13, 15]),
        creer_etudiant("Claire Petit", 21, [18, 19, 17, 20]),
        creer_etudiant("David Roux", 20, [8, 9, 7, 10]),
        creer_etudiant("Emma Blanc", 19, [16, 15, 17, 16])
    ]

    # Afficher toutes les statistiques
    afficher("=== Tous les étudiants ===")
    afficher_statistiques(etudiants)

    # Filtrer les étudiants ayant réussi
    reussis = filtrer_reussis(etudiants, 12)

    afficher("\n=== Étudiants ayant réussi (moyenne >= 12) ===")
    afficher_statistiques(reussis)

    # Trier par moyenne (décroissant)
    etudiants_tries = trier(etudiants, key=lambda e: e["moyenne"], reverse=Vrai)

    afficher("\n=== Classement par moyenne ===")
    pour rang, etudiant dans enumerer(etudiants_tries, 1):
        afficher(f"{rang}. {etudiant['nom']}: {etudiant['moyenne']:.2f}")

# Point d'entrée
si __name__ == "__main__":
    principale()

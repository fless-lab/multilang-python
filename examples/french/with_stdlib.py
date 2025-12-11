# multilang-python: fr
"""
Exemple d'utilisation des wrappers stdlib en français.

Ce fichier montre comment utiliser les modules standards Python
avec des noms français grâce aux wrappers.
"""

depuis multilang_python.stdlib.fr importer systeme, json

fonction principale():
    """Démontre l'utilisation des wrappers français."""

    afficher("=== Exemple avec wrappers stdlib français ===\n")

    # 1. Opérations sur les fichiers/dossiers
    afficher("1. Vérification de fichiers:")
    si systeme.chemin_existe("."):
        afficher("  ✓ Le dossier courant existe")
        afficher(f"  - Dossier actuel: {systeme.obtenir_cwd()}")

    # 2. Lister les fichiers
    afficher("\n2. Liste des fichiers:")
    essayer:
        fichiers = systeme.lister_dossier(".")
        afficher(f"  - {longueur(fichiers)} fichiers trouvés")
        pour fichier dans fichiers[:5]:  # Afficher les 5 premiers
            afficher(f"    • {fichier}")
    sauf Exception comme e:
        afficher(f"  Erreur: {e}")

    # 3. Manipulation JSON
    afficher("\n3. Manipulation JSON:")
    donnees = {
        "nom": "multilang-python",
        "version": "1.0",
        "langues": ["français", "espagnol", "allemand"]
    }

    # Convertir en JSON
    json_texte = json.dumper(donnees)
    afficher("  - Données en JSON:")
    afficher(f"    {json_texte}")

    # Recharger depuis JSON
    donnees_rechargees = json.charger(json_texte)
    afficher(f"  - Nom rechargé: {donnees_rechargees['nom']}")
    afficher(f"  - Nombre de langues: {longueur(donnees_rechargees['langues'])}")

    # 4. Exemple avec traitement de liste
    afficher("\n4. Traitement de données:")
    nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Filtrer les nombres pairs
    pairs = liste(filtrer(lambda x: x % 2 == 0, nombres))
    afficher(f"  - Nombres pairs: {pairs}")

    # Calculer la somme
    total = somme(pairs)
    afficher(f"  - Somme des pairs: {total}")

    # Moyenne
    moyenne = total / longueur(pairs)
    afficher(f"  - Moyenne: {moyenne}")

    afficher("\n✓ Exemple terminé avec succès!")


# Point d'entrée
si __name__ == "__main__":
    principale()

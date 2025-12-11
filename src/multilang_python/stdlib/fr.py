"""
Wrappers français pour modules Python standards.

Ces wrappers permettent d'utiliser des noms français pour les fonctions
de la bibliothèque standard Python.

Exemple:
    # multilang-python: fr
    depuis multilang_python.stdlib.fr importer systeme, json

    si systeme.chemin_existe("fichier.txt"):
        donnees = json.charger('{"test": 1}')
"""

import os
import json as _json
import sys as _sys


class Systeme:
    """Wrapper français pour le module os."""

    @staticmethod
    def chemin_existe(chemin):
        """Vérifie si un chemin existe."""
        return os.path.exists(chemin)

    @staticmethod
    def lister_dossier(chemin="."):
        """Liste les fichiers d'un dossier."""
        return os.listdir(chemin)

    @staticmethod
    def creer_dossier(chemin):
        """Crée un dossier."""
        return os.makedirs(chemin, exist_ok=True)

    @staticmethod
    def supprimer_fichier(chemin):
        """Supprime un fichier."""
        return os.remove(chemin)

    @staticmethod
    def obtenir_cwd():
        """Obtient le répertoire de travail actuel."""
        return os.getcwd()


class JsonFr:
    """Wrapper français pour le module json."""

    @staticmethod
    def charger(texte):
        """Charge du JSON depuis une chaîne."""
        return _json.loads(texte)

    @staticmethod
    def charger_fichier(fichier):
        """Charge du JSON depuis un fichier."""
        return _json.load(fichier)

    @staticmethod
    def dumper(obj):
        """Convertit un objet Python en JSON."""
        return _json.dumps(obj, ensure_ascii=False, indent=2)

    @staticmethod
    def dumper_fichier(obj, fichier):
        """Écrit un objet Python en JSON dans un fichier."""
        return _json.dump(obj, fichier, ensure_ascii=False, indent=2)


class SysFr:
    """Wrapper français pour le module sys."""

    @staticmethod
    def quitter(code=0):
        """Quitte le programme."""
        return _sys.exit(code)

    @staticmethod
    def arguments():
        """Retourne les arguments de ligne de commande."""
        return _sys.argv

    @staticmethod
    def version():
        """Retourne la version de Python."""
        return _sys.version


# Instances globales pour import direct
systeme = Systeme()
json = JsonFr()
sys = SysFr()

# Wrappers Standard Library

## Le Problème

Le transpileur multilang-python traduit les **keywords** et **built-in functions** Python, mais **PAS** les modules de la bibliothèque standard.

### Ce qui est traduit automatiquement :
```python
# multilang-python: fr
pour i dans intervalle(10):  # ✅ Traduit: for i in range(10)
    afficher(i)               # ✅ Traduit: print(i)
```

### Ce qui N'est PAS traduit :
```python
# multilang-python: fr
importer json
importer os

# ❌ json.loads et os.path.exists restent en anglais
donnees = json.loads('{"test": 1}')
si os.path.exists("fichier.txt"):
    afficher("OK")
```

## La Solution : Wrappers Optionnels

Nous fournissons des **wrappers optionnels** qui donnent des noms français (ou autres langues) aux fonctions de la stdlib.

### Utilisation

```python
# multilang-python: fr
depuis multilang_python.stdlib.fr importer systeme, json

# Maintenant vous pouvez utiliser des noms français !
si systeme.chemin_existe("fichier.txt"):
    donnees = json.charger('{"nom": "test"}')
    afficher(donnees)
```

## Modules Disponibles

### 🇫🇷 Français (`multilang_python.stdlib.fr`)

#### `systeme` (wrapper pour `os`)
```python
systeme.chemin_existe(chemin)      # os.path.exists()
systeme.lister_dossier(chemin)     # os.listdir()
systeme.creer_dossier(chemin)      # os.makedirs()
systeme.supprimer_fichier(chemin)  # os.remove()
systeme.obtenir_cwd()              # os.getcwd()
```

#### `json` (wrapper pour `json`)
```python
json.charger(texte)             # json.loads()
json.charger_fichier(fichier)   # json.load()
json.dumper(obj)                # json.dumps()
json.dumper_fichier(obj, f)     # json.dump()
```

#### `sys` (wrapper pour `sys`)
```python
sys.quitter(code)               # sys.exit()
sys.arguments()                 # sys.argv
sys.version()                   # sys.version
```

## Exemples Complets

### Manipulation de Fichiers (Français)

```python
# multilang-python: fr
depuis multilang_python.stdlib.fr importer systeme

fonction lister_fichiers_python(dossier="."):
    """Liste tous les fichiers .py dans un dossier."""
    essayer:
        fichiers = systeme.lister_dossier(dossier)
        fichiers_py = [f pour f dans fichiers si f.endswith(".py")]
        retourner fichiers_py
    sauf Exception comme e:
        afficher(f"Erreur: {e}")
        retourner []

# Utilisation
fichiers = lister_fichiers_python()
afficher(f"Trouvé {longueur(fichiers)} fichiers Python")
```

### JSON et Données (Français)

```python
# multilang-python: fr
depuis multilang_python.stdlib.fr importer json

fonction sauvegarder_config(config, fichier):
    """Sauvegarde une configuration en JSON."""
    avec ouvrir(fichier, 'w') comme f:
        json.dumper_fichier(config, f)
    afficher(f"Configuration sauvegardée dans {fichier}")

fonction charger_config(fichier):
    """Charge une configuration depuis JSON."""
    avec ouvrir(fichier, 'r') comme f:
        retourner json.charger_fichier(f)

# Utilisation
config = {
    "langue": "français",
    "mode": "débogage",
    "port": 8000
}

sauvegarder_config(config, "config.json")
config_chargee = charger_config("config.json")
afficher(config_chargee)
```

## Pourquoi cette Approche ?

### ✅ Avantages

1. **Optionnel** : Vous choisissez d'utiliser les wrappers ou pas
2. **Flexible** : Mélangez anglais et français selon vos besoins
3. **Compatible** : Toute la documentation Python reste utilisable
4. **Extensible** : Facile d'ajouter de nouveaux wrappers
5. **Maintenable** : Pas besoin de maintenir des milliers de traductions

### ❌ Alternative (non retenue) : Tout traduire automatiquement

Problèmes si on traduisait automatiquement tous les modules :

1. **Volume** : Des milliers de fonctions dans la stdlib
2. **Maintenance** : Mettre à jour à chaque nouvelle version Python
3. **Ambiguïté** : Certains noms sont difficiles à traduire
4. **Documentation** : Incompatible avec docs.python.org
5. **Packages tiers** : Impossible de traduire numpy, requests, etc.

## Contribuer

Vous pouvez ajouter des wrappers pour :

1. **Plus de modules** : datetime, pathlib, collections, etc.
2. **D'autres langues** : Espagnol, Allemand, etc.

### Exemple : Ajouter un wrapper

```python
# src/multilang_python/stdlib/fr.py

class DateHeure:
    """Wrapper français pour datetime."""

    @staticmethod
    def maintenant():
        """Retourne la date/heure actuelle."""
        import datetime
        return datetime.datetime.now()

    @staticmethod
    def aujourdhui():
        """Retourne la date d'aujourd'hui."""
        import datetime
        return datetime.date.today()

# Exporter
date_heure = DateHeure()
```

## Résumé

| Approche | Avantages | Inconvénients |
|----------|-----------|---------------|
| **Keywords/Builtins seulement** (actuel) | Simple, maintenable | Mélange français/anglais |
| **Wrappers optionnels** (recommandé) | Flexible, extensible | Nécessite import explicite |
| **Tout traduire automatiquement** | "Pur" linguistiquement | Impossible à maintenir |

**Notre choix** : Wrappers optionnels pour le meilleur équilibre !

## Voir Aussi

- [Exemples avec stdlib](../examples/french/with_stdlib.py)
- [Ajouter une langue](../CONTRIBUTING.md)
- [API Documentation](API.md)

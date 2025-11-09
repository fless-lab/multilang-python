# 🎬 Fichiers de Démonstration

Ce dossier contient des exemples prêts à l'emploi pour démontrer **multilang-python** en live.

## 🚀 Démarrage Ultra-Rapide

### Option 1: Exécuter toutes les démos (recommandé)

```bash
bash demo/RUN_ALL_DEMOS.sh
```

Ce script exécute toutes les démos dans l'ordre avec des pauses entre chacune.

### Option 2: Exécuter une démo spécifique

```bash
# Démo 1: Hello World (1 min)
multilang-python demo/01_hello.py

# Démo 2: Calculatrice (2 min)
multilang-python demo/02_calculatrice.py

# Démo 3: Analyse de données (3 min)
multilang-python demo/03_analyse_donnees.py

# Démo 4A: Espagnol (1 min)
multilang-python demo/04_multilangue_es.py

# Démo 4B: Allemand (1 min)
multilang-python demo/04_multilangue_de.py

# Démo 5: POO (3 min)
multilang-python demo/05_classes_oop.py
```

## 📋 Liste des Démos

| Fichier | Durée | Concepts | Niveau |
|---------|-------|----------|--------|
| `01_hello.py` | 1 min | Fonctions de base | Débutant |
| `02_calculatrice.py` | 2 min | Si/Sinon, Boucles | Débutant |
| `03_analyse_donnees.py` | 3 min | Lambda, Filtrer, Stats | Intermédiaire |
| `04_multilangue_es.py` | 1 min | Multi-langues (ES) | Débutant |
| `04_multilangue_de.py` | 1 min | Multi-langues (DE) | Débutant |
| `05_classes_oop.py` | 3 min | Classes, Héritage | Avancé |

## 🎯 Plan de Démo Suggéré (15 min)

### Introduction (2 min)
- Expliquer le concept
- Montrer `multilang-python --list-langs`

### Démos Pratiques (10 min)
1. **01_hello.py** - Montrer la simplicité
2. **02_calculatrice.py** - Montrer les structures de contrôle
3. **04_multilangue_es.py** + **04_multilangue_de.py** - Montrer multi-langues
4. **03_analyse_donnees.py** OU **05_classes_oop.py** - Montrer les features avancées

### Outils (2 min)
- `python scripts/validate_all.py`
- `multilang-python demo.py --output traduit.py`

### Conclusion (1 min)
- Récapituler les forces
- Mentionner GitHub
- Questions

## 💡 Tips pour une Démo Réussie

### Avant la Démo
```bash
# Vérifier que tout fonctionne
bash demo/RUN_ALL_DEMOS.sh

# Agrandir la police du terminal
# Ctrl+Plus (Linux/Windows) ou Cmd+Plus (Mac)
```

### Pendant la Démo
1. **Commenter en temps réel** - Expliquer ce que fait le code
2. **Montrer le fichier source** - `cat demo/01_hello.py`
3. **Montrer la traduction** - `multilang-python demo/01_hello.py --output traduit.py && cat traduit.py`
4. **Alterner langues** - Montrer français, espagnol, allemand
5. **Interagir** - Poser des questions à l'audience

### Points Clés à Mentionner
- ✅ **7 langues** supportées
- ✅ **Zero dépendances** - uniquement stdlib
- ✅ **35 keywords + 60+ builtins**
- ✅ **100% testé** - 25 tests passants
- ✅ **Open Source** - Contributions bienvenues
- ✅ **Éducation** - Parfait pour enseigner Python

## 🎨 Personnalisation

Vous pouvez créer vos propres démos:

```python
# demo/ma_demo.py
# multilang-python: fr

fonction ma_fonction():
    afficher("Ma démo personnalisée!")

ma_fonction()
```

Puis l'exécuter:
```bash
multilang-python demo/ma_demo.py
```

## 📊 Exemples de Sortie

### Démo 1: Hello World
```
🎉 Bonjour, Paris!
Bienvenue dans multilang-python!
Vous programmez en FRANÇAIS! 🇫🇷

✅ Ce code est 100% en français et fonctionne comme du Python!
```

### Démo 2: Calculatrice
```
══════════════════════════════════════════════════
         🧮 CALCULATRICE EN FRANÇAIS 🧮
══════════════════════════════════════════════════

  10 + 5 = 15
  10 - 5 = 5
  10 * 5 = 50
  10 / 5 = 2.0
  10 / 0 = ❌ Erreur: Division par zéro!

✅ Si/Sinon, Fonctions, Boucles... tout en français!
```

## 🔧 Troubleshooting

### "multilang-python: command not found"
```bash
# Réinstaller
pip install -e .

# Ou utiliser directement
python -m multilang_python demo/01_hello.py
```

### Les caractères spéciaux ne s'affichent pas
```bash
# Vérifier l'encodage du terminal
export LANG=fr_FR.UTF-8
```

### Script bash ne fonctionne pas
```bash
# Rendre le script exécutable
chmod +x demo/RUN_ALL_DEMOS.sh

# Ou l'exécuter avec bash
bash demo/RUN_ALL_DEMOS.sh
```

## 📚 Ressources Supplémentaires

- **Guide de Démo Complet**: `docs/DEMO_GUIDE.md`
- **Exemples Avancés**: `examples/french/`, `examples/spanish/`
- **Documentation**: `README.md`

## 🎬 Bonne Démo!

N'oublie pas:
1. Être enthousiaste! 🎉
2. Expliquer clairement 📢
3. Interagir avec l'audience 👥
4. Avoir fun! 🚀

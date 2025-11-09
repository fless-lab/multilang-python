# 📋 Cheat Sheet - multilang-python

Référence rapide pour la démo live.

---

## 🚀 Installation One-Liner

```bash
git clone https://github.com/fless-lab/multilang-python.git && cd multilang-python && pip install -e . && multilang-python --version
```

---

## ⌨️ Commandes Essentielles

```bash
# Exécuter un fichier
multilang-python fichier.py

# Sauvegarder la traduction
multilang-python fichier.py --output traduit.py

# Spécifier la langue
multilang-python fichier.py --lang fr

# Lister les langues
multilang-python --list-langs

# Version
multilang-python --version

# Aide
multilang-python --help
```

---

## 🎬 Démos Quick Launch

```bash
# Toutes les démos
bash demo/RUN_ALL_DEMOS.sh

# Démos individuelles
multilang-python demo/01_hello.py              # Hello World (1min)
multilang-python demo/02_calculatrice.py       # Calculatrice (2min)
multilang-python demo/03_analyse_donnees.py    # Analyse (3min)
multilang-python demo/04_multilangue_es.py     # Espagnol (1min)
multilang-python demo/04_multilangue_de.py     # Allemand (1min)
multilang-python demo/05_classes_oop.py        # POO (3min)
```

---

## 🔧 Outils Développeur

```bash
# Valider toutes les langues
python scripts/validate_all.py

# Ajouter une langue (interactif)
python scripts/add_language.py

# Mode watch
python scripts/watch.py examples/french/*.py --output translated/

# Setup dev
python scripts/setup_dev.py

# Tests
pytest tests/unit/test_transpiler.py -v
```

---

## 📝 Snippets de Code Prêts

### Exemple Minimal
```bash
echo -e '# multilang-python: fr\n\nafficher("Hello!")' > test.py && multilang-python test.py
```

### Boucle Simple
```bash
cat > boucle.py << 'EOF'
# multilang-python: fr
pour i dans intervalle(5):
    afficher(f"Numéro {i}")
EOF
multilang-python boucle.py
```

### Fonction
```bash
cat > fonction.py << 'EOF'
# multilang-python: fr
fonction double(x):
    retourner x * 2

afficher(double(21))
EOF
multilang-python fonction.py
```

---

## 🌐 Mots-Clés par Langue

### Français
```
fonction, si, sinon, sinon_si, pour, tant_que, retourner
afficher, longueur, intervalle, entier, chaîne
```

### Espagnol
```
funcion, si, sino, si_no, para, mientras, retornar
mostrar, longitud, rango, entero, cadena
```

### Allemand
```
funktion, wenn, sonst, sonst_wenn, fuer, waehrend, zurueck
drucken, laenge, bereich, ganzzahl, zeichenkette
```

---

## 💡 Points Clés à Mentionner

- ✅ **7 langues** - FR, ES, DE, PT, IT, AR, ZH
- ✅ **35 keywords** - Tous les mots-clés Python
- ✅ **60+ builtins** - print, len, range, map, filter, etc.
- ✅ **Zero dépendances** - Uniquement stdlib
- ✅ **100% testé** - 25 tests passants
- ✅ **Protection strings** - Les strings ne sont pas traduites
- ✅ **Extensible** - Facile d'ajouter des langues
- ✅ **Open Source** - MIT License

---

## 🎯 Structure de Démo (15 min)

1. **Intro** (2min) - Concept + `--list-langs`
2. **Hello** (2min) - `demo/01_hello.py`
3. **Calculatrice** (2min) - `demo/02_calculatrice.py`
4. **Multi-langues** (2min) - ES + DE
5. **Avancé** (4min) - Analyse ou POO
6. **Outils** (2min) - Validation, traduction
7. **Conclusion** (1min) - Récap + GitHub

---

## 🆘 Troubleshooting Rapide

```bash
# Command not found
pip install -e .

# Module not found
cd multilang-python && pip install -e .

# Tests fail
pip install pytest && pytest tests/

# Encoding issues
export LANG=fr_FR.UTF-8
```

---

## 🔗 Liens Utiles

- **Repo:** github.com/fless-lab/multilang-python
- **Guide Démo:** docs/DEMO_GUIDE.md
- **Quick Start:** QUICKSTART.md
- **Exemples:** examples/ et demo/

---

## 📊 Statistiques Impressionnantes

- **2,324 lignes** de code ajoutées
- **22 fichiers** modifiés
- **7 langues** complètes
- **25 tests** (100% passing)
- **0 erreurs** de validation

---

**🎬 Prêt pour la démo! Go go go! 🚀**

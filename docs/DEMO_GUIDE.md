# 🎬 Guide de Démo LIVE - multilang-python

Guide complet pour une démonstration impressionnante en direct.

---

## ⚡ Setup Rapide (5 minutes)

### 1. Cloner et Installer

```bash
# 1. Cloner le repo
git clone https://github.com/fless-lab/multilang-python.git
cd multilang-python

# 2. Installer (choisir UNE option)

# Option A: Installation directe (rapide)
pip install -e .

# Option B: Avec environnement virtuel (recommandé)
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
pip install -e .

# 3. Vérifier l'installation
multilang-python --version
multilang-python --list-langs
```

**Sortie attendue:**
```
multilang-python 0.1.0

Langues disponibles:
  fr  - French
  es  - Spanish
  de  - German
  pt  - Portuguese
  it  - Italian
  ar  - Arabic
  zh  - Chinese
```

---

## 🎯 Démo Niveau 1: "Hello World" (2 minutes)

### Créer un fichier simple

```bash
# Créer demo_fr.py
cat > demo_fr.py << 'EOF'
# multilang-python: fr

fonction saluer(nom):
    afficher(f"Bonjour, {nom}!")
    afficher("Bienvenue dans multilang-python 🚀")

saluer("Paris")
EOF
```

### Exécuter

```bash
# Exécuter directement
multilang-python demo_fr.py

# Voir la traduction
multilang-python demo_fr.py --output demo_fr_translated.py
cat demo_fr_translated.py
```

**Points à mentionner:**
- ✅ Code 100% en français
- ✅ S'exécute comme du Python normal
- ✅ Simple header `# multilang-python: fr`

---

## 🚀 Démo Niveau 2: Calculatrice Interactive (3 minutes)

```bash
cat > calculatrice.py << 'EOF'
# multilang-python: fr

fonction calculer(a, b, operation):
    si operation == "+":
        retourner a + b
    sinon_si operation == "-":
        retourner a - b
    sinon_si operation == "*":
        retourner a * b
    sinon_si operation == "/":
        si b != 0:
            retourner a / b
        sinon:
            retourner "Erreur: division par zéro!"
    sinon:
        retourner "Opération invalide!"

# Tests
afficher("=== Calculatrice en Français ===")
afficher(f"10 + 5 = {calculer(10, 5, '+')}")
afficher(f"10 - 5 = {calculer(10, 5, '-')}")
afficher(f"10 * 5 = {calculer(10, 5, '*')}")
afficher(f"10 / 5 = {calculer(10, 5, '/')}")
afficher(f"10 / 0 = {calculer(10, 0, '/')}")
EOF

multilang-python calculatrice.py
```

**Points à mentionner:**
- ✅ `si`/`sinon_si`/`sinon` = `if`/`elif`/`else`
- ✅ `fonction` = `def`
- ✅ `afficher` = `print`
- ✅ Code lisible pour les francophones

---

## 💎 Démo Niveau 3: Traitement de Données (5 minutes)

```bash
cat > analyse_donnees.py << 'EOF'
# multilang-python: fr

fonction analyser_nombres(liste_nombres):
    """Analyse une liste de nombres."""

    # Filtrer les nombres pairs
    pairs = liste(filtrer(lambda x: x % 2 == 0, liste_nombres))

    # Filtrer les nombres impairs
    impairs = liste(filtrer(lambda x: x % 2 != 0, liste_nombres))

    # Statistiques
    total = somme(liste_nombres)
    moyenne = total / longueur(liste_nombres)

    retourner {
        "total": total,
        "moyenne": moyenne,
        "pairs": pairs,
        "impairs": impairs,
        "max": maximum(liste_nombres),
        "min": minimum(liste_nombres)
    }

# Exemple d'utilisation
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

afficher("=== Analyse de Données en Français ===")
afficher(f"Nombres: {nombres}")
afficher()

resultats = analyser_nombres(nombres)

afficher(f"📊 Total: {resultats['total']}")
afficher(f"📈 Moyenne: {resultats['moyenne']}")
afficher(f"➡️  Pairs: {resultats['pairs']}")
afficher(f"➡️  Impairs: {resultats['impairs']}")
afficher(f"⬆️  Maximum: {resultats['max']}")
afficher(f"⬇️  Minimum: {resultats['min']}")
EOF

multilang-python analyse_donnees.py
```

**Points à mentionner:**
- ✅ Fonctions avancées: `filtrer`, `somme`, `longueur`, `maximum`, `minimum`
- ✅ Lambda functions
- ✅ Dictionnaires et listes
- ✅ Code production-ready

---

## 🌍 Démo Niveau 4: Multi-langues (3 minutes)

### Espagnol

```bash
cat > hola.py << 'EOF'
# multilang-python: es

funcion saludar(nombre):
    mostrar(f"¡Hola, {nombre}!")
    mostrar("¡Bienvenido a multilang-python!")

para i en rango(3):
    saludar(f"Usuario {i+1}")
EOF

multilang-python hola.py
```

### Allemand

```bash
cat > hallo.py << 'EOF'
# multilang-python: de

funktion gruessen(name):
    drucken(f"Hallo, {name}!")

fuer i in bereich(5):
    gruessen(f"Benutzer {i+1}")
EOF

multilang-python hallo.py
```

**Points à mentionner:**
- ✅ 7 langues supportées
- ✅ Même syntaxe, juste traduite
- ✅ Extensible à toute langue

---

## 🔥 Démo Niveau 5: Features Avancées

### 1. Async/Await (si Python 3.7+)

```bash
cat > async_demo.py << 'EOF'
# multilang-python: fr

importer asyncio

asynchrone fonction tache(nom, duree):
    afficher(f"Début {nom}")
    attendre asyncio.sleep(duree)
    afficher(f"Fin {nom}")
    retourner f"Résultat de {nom}"

asynchrone fonction principal():
    afficher("=== Demo Async en Français ===")
    resultat = attendre tache("Tâche 1", 1)
    afficher(resultat)

asyncio.run(principal())
EOF

multilang-python async_demo.py
```

### 2. Classes et OOP

```bash
cat > classes.py << 'EOF'
# multilang-python: fr

classe Personne:
    fonction __init__(soi, nom, age):
        soi.nom = nom
        soi.age = age

    fonction presenter(soi):
        afficher(f"Je suis {soi.nom}, j'ai {soi.age} ans")

classe Etudiant(Personne):
    fonction __init__(soi, nom, age, ecole):
        super().__init__(nom, age)
        soi.ecole = ecole

    fonction presenter(soi):
        afficher(f"Je suis {soi.nom}, j'ai {soi.age} ans")
        afficher(f"J'étudie à {soi.ecole}")

# Utilisation
p = Personne("Alice", 30)
e = Etudiant("Bob", 20, "Sorbonne")

p.presenter()
afficher()
e.presenter()
EOF

multilang-python classes.py
```

### 3. Gestion d'Erreurs

```bash
cat > erreurs.py << 'EOF'
# multilang-python: fr

fonction diviser(a, b):
    essayer:
        resultat = a / b
        afficher(f"{a} / {b} = {resultat}")
        retourner resultat
    sauf ZeroDivisionError comme e:
        afficher(f"Erreur: Division par zéro!")
        retourner Aucun
    finalement:
        afficher("Opération terminée")

# Tests
diviser(10, 2)
afficher()
diviser(10, 0)
EOF

multilang-python erreurs.py
```

---

## 🛠️ Outils Développeur

### Valider les langues

```bash
python scripts/validate_all.py
```

### Mode Watch (auto-compile)

```bash
# Surveiller un dossier et auto-traduire
python scripts/watch.py examples/french/*.py --output translated/
```

### Ajouter une langue

```bash
python scripts/add_language.py
# Suivre les instructions interactives
```

---

## 🎤 Script de Présentation Complet (10-15 min)

### Introduction (1 min)
```
"Bonjour! Aujourd'hui je vais vous montrer multilang-python,
un transpileur qui permet d'écrire du Python dans n'importe quelle langue.

Pourquoi? Pour rendre la programmation accessible aux non-anglophones,
particulièrement dans l'éducation."
```

### Démo 1: Hello World (2 min)
```bash
# Montrer demo_fr.py
multilang-python demo_fr.py

# Montrer la traduction
multilang-python demo_fr.py --output traduit.py
cat traduit.py
```

**Dire:**
"Vous voyez, le code est 100% en français, mais s'exécute comme du Python normal!"

### Démo 2: Calculatrice (3 min)
```bash
multilang-python calculatrice.py
```

**Dire:**
"On peut utiliser toutes les structures de contrôle: si/sinon, fonctions, etc."

### Démo 3: Multi-langues (2 min)
```bash
# Français
multilang-python demo_fr.py

# Espagnol
multilang-python hola.py

# Allemand
multilang-python hallo.py
```

**Dire:**
"On supporte 7 langues: français, espagnol, allemand, portugais, italien, arabe, chinois!"

### Démo 4: Features Avancées (3 min)
```bash
# Classes
multilang-python classes.py

# Async
multilang-python async_demo.py
```

**Dire:**
"Toutes les features modernes de Python sont supportées: async/await, classes, exceptions..."

### Démo 5: Outils (2 min)
```bash
# Validation
python scripts/validate_all.py

# Liste des langues
multilang-python --list-langs
```

**Dire:**
"Le projet inclut des outils pour valider, ajouter des langues, et plus encore."

### Conclusion (1 min)
```
"multilang-python, c'est:
- 7 langues
- 35 keywords + 60+ builtins
- 0 dépendances
- 100% open source
- Prêt pour l'éducation

Le code est sur GitHub: github.com/fless-lab/multilang-python
Merci!"
```

---

## 🎯 Points Clés à Mentionner

### Forces du Projet
1. **Zero Dépendances** - Uniquement stdlib Python
2. **7 Langues** - Fr, Es, De, Pt, It, Ar, Zh
3. **Complet** - 35 keywords, 60+ builtins
4. **Testé** - 25 tests, 100% passing
5. **Extensible** - Ajout facile de nouvelles langues
6. **Performant** - Cache intelligent
7. **Production-ready** - Protection strings/comments

### Use Cases
1. **Éducation** - Enseigner Python aux non-anglophones
2. **Accessibilité** - Démocratiser la programmation
3. **Transition** - Apprendre avec sa langue, puis migrer vers l'anglais
4. **Prototyping rapide** - Pour ceux plus à l'aise dans leur langue

---

## ⚠️ Troubleshooting Rapide

### Problème: "multilang-python: command not found"
```bash
# Réinstaller
pip install -e .

# Ou utiliser Python directement
python -m multilang_python demo_fr.py
```

### Problème: "No module named 'multilang_python'"
```bash
# Vérifier que vous êtes dans le bon dossier
cd multilang-python
pip install -e .
```

### Problème: Tests échouent
```bash
# Installer les dépendances de test
pip install pytest pytest-cov

# Relancer
pytest tests/unit/test_transpiler.py -v
```

---

## 📋 Checklist Avant Démo

- [ ] Repo cloné
- [ ] Package installé (`pip install -e .`)
- [ ] `multilang-python --version` fonctionne
- [ ] `multilang-python --list-langs` fonctionne
- [ ] Exemples créés (demo_fr.py, calculatrice.py, etc.)
- [ ] Tous les exemples testés
- [ ] Terminal propre et lisible
- [ ] Police de terminal assez grande
- [ ] Internet (si besoin de montrer GitHub)

---

## 🎬 Exemples Prêts à l'Emploi

Tous les exemples sont dans `examples/`:
- `examples/french/hello_world.py`
- `examples/french/calculator.py`
- `examples/french/data_processing.py`
- `examples/spanish/calculator.py`

Tu peux les utiliser directement:
```bash
multilang-python examples/french/calculator.py
multilang-python examples/french/data_processing.py
```

---

## 💡 Tips pour une Démo Réussie

1. **Commencer Simple** - Hello World puis complexifier
2. **Montrer la Traduction** - Utiliser `--output` pour montrer le Python généré
3. **Multi-langues** - Alterner entre 2-3 langues
4. **Features Modernes** - Montrer async/await, classes
5. **Interaction** - Poser des questions à l'audience
6. **Enthousiasme** - Montrer ta passion pour le projet!

---

## 🚀 Commandes Rapides Copy-Paste

```bash
# Setup complet en une commande
git clone https://github.com/fless-lab/multilang-python.git && cd multilang-python && pip install -e . && multilang-python --version

# Créer et exécuter un exemple rapide
echo -e '# multilang-python: fr\n\npour i dans intervalle(5):\n    afficher(f"Bonjour numéro {i+1}")' > demo.py && multilang-python demo.py

# Voir toutes les langues
multilang-python --list-langs

# Valider tout
python scripts/validate_all.py
```

---

**Bonne démo! 🎉**

# ⚡ Quick Start - multilang-python

Guide ultra-rapide pour commencer en **moins de 5 minutes**.

---

## 🚀 Installation (2 minutes)

```bash
# 1. Cloner
git clone https://github.com/fless-lab/multilang-python.git
cd multilang-python

# 2. Installer
pip install -e .

# 3. Vérifier
multilang-python --version
```

**Sortie attendue:** `multilang-python 0.1.0`

---

## 🎯 Premier Programme (1 minute)

```bash
# Créer un fichier
cat > hello.py << 'EOF'
# multilang-python: fr

fonction saluer(nom):
    afficher(f"Bonjour, {nom}!")

saluer("Monde")
EOF

# Exécuter
multilang-python hello.py
```

**Sortie:** `Bonjour, Monde!`

---

## 🌍 Langues Disponibles

```bash
multilang-python --list-langs
```

**Langues:** Français (fr), Espagnol (es), Allemand (de), Portugais (pt), Italien (it), Arabe (ar), Chinois (zh)

---

## 📚 Exemples Rapides

### Français
```python
# multilang-python: fr
pour i dans intervalle(5):
    afficher(f"Nombre {i}")
```

### Espagnol
```python
# multilang-python: es
para i en rango(5):
    mostrar(f"Número {i}")
```

### Allemand
```python
# multilang-python: de
fuer i in bereich(5):
    drucken(f"Nummer {i}")
```

---

## 🛠️ Commandes Utiles

```bash
# Exécuter
multilang-python fichier.py

# Sauvegarder la traduction
multilang-python fichier.py --output traduit.py

# Lister les langues
multilang-python --list-langs

# Voir la version
multilang-python --version
```

---

## 🎬 Démos Prêtes à l'Emploi

```bash
# Exécuter toutes les démos
bash demo/RUN_ALL_DEMOS.sh

# Ou une seule
multilang-python demo/01_hello.py
multilang-python demo/02_calculatrice.py
multilang-python demo/03_analyse_donnees.py
```

---

## 📖 Plus d'Infos

- **Guide de Démo Live:** `docs/DEMO_GUIDE.md`
- **Documentation Complète:** `README.md`
- **Wrappers Stdlib:** `docs/STDLIB_WRAPPERS.md`

---

**C'est tout! Vous êtes prêt! 🎉**

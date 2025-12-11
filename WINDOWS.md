# Installation Windows - multilang-python

Guide spécifique pour installer multilang-python sur Windows.

---

## Installation Rapide

### Prérequis
- Python 3.7+ installé
- Git pour Windows
- PowerShell ou CMD

### Méthode 1: Installation Standard (Recommandée)

```powershell
# 1. Cloner le repo
git clone https://github.com/fless-lab/multilang-python.git
cd multilang-python

# 2. Créer un environnement virtuel
python -m venv venv

# 3. Activer l'environnement virtuel
.\venv\Scripts\activate

# 4. Installer
pip install -e .

# 5. Vérifier
multilang-python --version
```

### Méthode 2: Sans Environnement Virtuel

```powershell
# 1. Cloner
git clone https://github.com/fless-lab/multilang-python.git
cd multilang-python

# 2. Installer directement
pip install -e .

# 3. Vérifier
multilang-python --version
```

---

## Problèmes Courants et Solutions

### Problème 1: UnicodeDecodeError lors de l'installation

**Erreur:**
```
UnicodeDecodeError: 'charmap' codec can't decode byte 0x8d
```

**Solution:**
```powershell
# Mettre à jour vers la dernière version du repo
git pull origin main

# Réinstaller
pip install -e .
```

**Cause:** Encodage UTF-8 dans setup.py (déjà fixé dans la dernière version)

---

### Problème 2: 'multilang-python' n'est pas reconnu

**Solution 1: Utiliser Python directement**
```powershell
python -m multilang_python fichier.py
```

**Solution 2: Ajouter au PATH**
```powershell
# Trouver le chemin Scripts
pip show multilang-python

# Ajouter manuellement au PATH système
# Panneau de configuration > Système > Variables d'environnement
# Ajouter: C:\Python310\Scripts (ou le chemin de votre Python)
```

**Solution 3: Réinstaller avec --user**
```powershell
pip uninstall multilang-python
pip install --user -e .
```

---

### Problème 3: Erreur lors de l'exécution des démos

**Erreur:**
```
bash: command not found
```

**Solution:** Utiliser PowerShell au lieu de bash
```powershell
# Au lieu de: bash demo/RUN_ALL_DEMOS.sh
# Exécuter manuellement:
multilang-python demo/01_hello.py
multilang-python demo/02_calculatrice.py
multilang-python demo/03_analyse_donnees.py
```

Ou créer un script PowerShell:
```powershell
# demo/RUN_ALL_DEMOS.ps1
Get-ChildItem demo/*.py | ForEach-Object {
    Write-Host "Executing $_..." -ForegroundColor Green
    multilang-python $_.FullName
    Write-Host ""
}
```

---

### Problème 4: Caractères spéciaux mal affichés

**Symptôme:**
```
�� au lieu de 🎉
```

**Solution:**
```powershell
# Définir l'encodage UTF-8 pour le terminal
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
chcp 65001

# Ou ajouter à votre profil PowerShell
notepad $PROFILE
# Ajouter: [Console]::OutputEncoding = [System.Text.Encoding]::UTF8
```

---

### Problème 5: Permission denied lors de l'installation

**Solution: Exécuter en tant qu'administrateur**
```powershell
# Clic droit sur PowerShell > Exécuter en tant qu'administrateur
# Puis relancer l'installation
```

Ou installer en mode utilisateur:
```powershell
pip install --user -e .
```

---

## Exécuter les Démos sur Windows

### Démos Individuelles (Simple)

```powershell
# Démo 1: Hello World
python -m multilang_python demo/01_hello.py

# Démo 2: Calculatrice
python -m multilang_python demo/02_calculatrice.py

# Démo 3: Analyse de données
python -m multilang_python demo/03_analyse_donnees.py

# Démo 4: Espagnol
python -m multilang_python demo/04_multilangue_es.py

# Démo 5: Allemand
python -m multilang_python demo/04_multilangue_de.py

# Démo 6: POO
python -m multilang_python demo/05_classes_oop.py
```

### Script PowerShell pour Toutes les Démos

Créer `demo/RUN_ALL_DEMOS.ps1`:
```powershell
Write-Host "╔════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║        DÉMONSTRATION MULTILANG-PYTHON                      ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

$demos = @(
    "demo/01_hello.py",
    "demo/02_calculatrice.py",
    "demo/03_analyse_donnees.py",
    "demo/04_multilangue_es.py",
    "demo/04_multilangue_de.py",
    "demo/05_classes_oop.py"
)

foreach ($demo in $demos) {
    Write-Host "`n═══════════════════════════════════════════════════════════" -ForegroundColor Yellow
    Write-Host "Exécution: $demo" -ForegroundColor Green
    Write-Host "═══════════════════════════════════════════════════════════`n" -ForegroundColor Yellow

    python -m multilang_python $demo

    Write-Host "`nAppuyez sur une touche pour continuer..." -ForegroundColor Cyan
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
}

Write-Host "`n Démonstration terminée!" -ForegroundColor Green
```

Puis exécuter:
```powershell
powershell -ExecutionPolicy Bypass -File demo/RUN_ALL_DEMOS.ps1
```

---

## Configuration Optimale pour Windows

### 1. Installer Windows Terminal (Recommandé)

Meilleur support UTF-8 et emojis:
```powershell
# Via Microsoft Store
winget install Microsoft.WindowsTerminal
```

### 2. Configurer UTF-8 par Défaut

Ajouter à `$PROFILE`:
```powershell
# Ouvrir le profil
notepad $PROFILE

# Ajouter ces lignes:
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
chcp 65001 | Out-Null
$env:PYTHONIOENCODING = "utf-8"
```

### 3. Installer Git Bash (Optionnel)

Pour exécuter les scripts `.sh`:
```powershell
# Via winget
winget install Git.Git

# Puis utiliser Git Bash
bash demo/RUN_ALL_DEMOS.sh
```

---

## Créer un Fichier Test Rapide

```powershell
# Créer un fichier de test
@"
# multilang-python: fr

fonction saluer(nom):
    afficher(f"Bonjour, {nom}!")

saluer("Windows")
"@ | Out-File -Encoding UTF8 test_fr.py

# L'exécuter
multilang-python test_fr.py
```

---

## Checklist Installation Windows

- [ ] Python 3.7+ installé (`python --version`)
- [ ] Git installé (`git --version`)
- [ ] Repo cloné
- [ ] Environnement virtuel créé et activé
- [ ] Package installé (`pip install -e .`)
- [ ] Commande fonctionne (`multilang-python --version`)
- [ ] UTF-8 configuré (emojis s'affichent correctement)
- [ ] Démos testées

---

## Support Supplémentaire

Si les problèmes persistent:

1. **Vérifier la version Python:**
   ```powershell
   python --version  # Doit être 3.7+
   ```

2. **Réinstaller complètement:**
   ```powershell
   # Supprimer l'environnement virtuel
   Remove-Item -Recurse -Force venv

   # Recréer
   python -m venv venv
   .\venv\Scripts\activate
   pip install --upgrade pip
   pip install -e .
   ```

3. **Utiliser Python directement:**
   ```powershell
   # Au lieu de multilang-python
   python -m multilang_python fichier.py
   ```

4. **Vérifier les logs d'erreur:**
   ```powershell
   pip install -e . --verbose
   ```

---

## Prêt pour la Démo!

Une fois installé, consulte:
- `QUICKSTART.md` - Guide rapide
- `CHEATSHEET.md` - Commandes de référence
- `docs/DEMO_GUIDE.md` - Guide de présentation complet

**Bon courage!**

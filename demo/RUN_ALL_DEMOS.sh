#!/bin/bash
# Script pour exécuter toutes les démos en séquence
# Usage: bash demo/RUN_ALL_DEMOS.sh

echo "╔════════════════════════════════════════════════════════════╗"
echo "║                                                            ║"
echo "║     🎬 DÉMONSTRATION MULTILANG-PYTHON 🎬                  ║"
echo "║                                                            ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
echo "Appuyez sur ENTRÉE pour commencer..."
read

# Fonction pour pause entre les démos
pause_demo() {
    echo ""
    echo "─────────────────────────────────────────────────────────────"
    echo ""
    echo "Appuyez sur ENTRÉE pour continuer vers la démo suivante..."
    read
}

# Démo 1: Hello World
echo "╔════════════════════════════════════════════════════════════╗"
echo "║  DÉMO 1: Hello World Simple (Français)                    ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
multilang-python demo/01_hello.py
pause_demo

# Démo 2: Calculatrice
echo "╔════════════════════════════════════════════════════════════╗"
echo "║  DÉMO 2: Calculatrice (Structures de Contrôle)            ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
multilang-python demo/02_calculatrice.py
pause_demo

# Démo 3: Analyse de Données
echo "╔════════════════════════════════════════════════════════════╗"
echo "║  DÉMO 3: Analyse de Données (Fonctions Avancées)          ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
multilang-python demo/03_analyse_donnees.py
pause_demo

# Démo 4A: Espagnol
echo "╔════════════════════════════════════════════════════════════╗"
echo "║  DÉMO 4A: Python en Espagnol 🇪🇸                          ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
multilang-python demo/04_multilangue_es.py
pause_demo

# Démo 4B: Allemand
echo "╔════════════════════════════════════════════════════════════╗"
echo "║  DÉMO 4B: Python en Allemand 🇩🇪                          ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
multilang-python demo/04_multilangue_de.py
pause_demo

# Démo 5: POO
echo "╔════════════════════════════════════════════════════════════╗"
echo "║  DÉMO 5: Programmation Orientée Objet                     ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
multilang-python demo/05_classes_oop.py
pause_demo

# Démo Extra: Langues disponibles
echo "╔════════════════════════════════════════════════════════════╗"
echo "║  LANGUES DISPONIBLES                                       ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
multilang-python --list-langs
echo ""

# Démo Extra: Validation
echo "╔════════════════════════════════════════════════════════════╗"
echo "║  VALIDATION DES LANGUES                                    ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
python scripts/validate_all.py
echo ""

# Conclusion
echo "╔════════════════════════════════════════════════════════════╗"
echo "║                                                            ║"
echo "║              ✅ DÉMONSTRATION TERMINÉE ✅                  ║"
echo "║                                                            ║"
echo "║  🌍 7 Langues | 35 Keywords | 60+ Builtins               ║"
echo "║  📦 Zero Dépendances | 🧪 100% Testé                     ║"
echo "║                                                            ║"
echo "║  GitHub: github.com/fless-lab/multilang-python            ║"
echo "║                                                            ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
echo "Merci! 🎉"

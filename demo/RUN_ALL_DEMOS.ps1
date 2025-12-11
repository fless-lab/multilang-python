# Script PowerShell pour exécuter toutes les démos multilang-python
# Usage: powershell -ExecutionPolicy Bypass -File demo/RUN_ALL_DEMOS.ps1

# Configuration UTF-8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8

# Couleurs
$ColorHeader = "Cyan"
$ColorSuccess = "Green"
$ColorDemo = "Yellow"
$ColorInfo = "White"

function Show-Banner {
    Write-Host "╔════════════════════════════════════════════════════════════╗" -ForegroundColor $ColorHeader
    Write-Host "║                                                            ║" -ForegroundColor $ColorHeader
    Write-Host "║     🎬 DÉMONSTRATION MULTILANG-PYTHON 🎬                  ║" -ForegroundColor $ColorHeader
    Write-Host "║                                                            ║" -ForegroundColor $ColorHeader
    Write-Host "╚════════════════════════════════════════════════════════════╝" -ForegroundColor $ColorHeader
    Write-Host ""
}

function Wait-Continue {
    Write-Host ""
    Write-Host "─────────────────────────────────────────────────────────────" -ForegroundColor $ColorDemo
    Write-Host ""
    Write-Host "Appuyez sur une touche pour continuer..." -ForegroundColor $ColorInfo
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
}

function Run-Demo {
    param(
        [string]$Title,
        [string]$File
    )

    Write-Host ""
    Write-Host "╔════════════════════════════════════════════════════════════╗" -ForegroundColor $ColorDemo
    Write-Host "║  $Title" -ForegroundColor $ColorDemo
    Write-Host "╚════════════════════════════════════════════════════════════╝" -ForegroundColor $ColorDemo
    Write-Host ""

    # Essayer multilang-python, sinon python -m
    try {
        & multilang-python $File 2>$null
        if ($LASTEXITCODE -ne 0) {
            throw
        }
    } catch {
        python -m multilang_python $File
    }
}

# Démarrage
Clear-Host
Show-Banner
Write-Host "Appuyez sur une touche pour commencer..." -ForegroundColor $ColorInfo
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

# Démo 1: Hello World
Run-Demo "DÉMO 1: Hello World Simple (Français)                    " "demo/01_hello.py"
Wait-Continue

# Démo 2: Calculatrice
Run-Demo "DÉMO 2: Calculatrice (Structures de Contrôle)            " "demo/02_calculatrice.py"
Wait-Continue

# Démo 3: Analyse de Données
Run-Demo "DÉMO 3: Analyse de Données (Fonctions Avancées)          " "demo/03_analyse_donnees.py"
Wait-Continue

# Démo 4A: Espagnol
Run-Demo "DÉMO 4A: Python en Espagnol 🇪🇸                          " "demo/04_multilangue_es.py"
Wait-Continue

# Démo 4B: Allemand
Run-Demo "DÉMO 4B: Python en Allemand 🇩🇪                          " "demo/04_multilangue_de.py"
Wait-Continue

# Démo 5: POO
Run-Demo "DÉMO 5: Programmation Orientée Objet                     " "demo/05_classes_oop.py"
Wait-Continue

# Langues disponibles
Write-Host ""
Write-Host "╔════════════════════════════════════════════════════════════╗" -ForegroundColor $ColorDemo
Write-Host "║  LANGUES DISPONIBLES                                       ║" -ForegroundColor $ColorDemo
Write-Host "╚════════════════════════════════════════════════════════════╝" -ForegroundColor $ColorDemo
Write-Host ""

try {
    & multilang-python --list-langs 2>$null
    if ($LASTEXITCODE -ne 0) {
        throw
    }
} catch {
    python -m multilang_python --list-langs
}

Write-Host ""
Wait-Continue

# Validation
Write-Host ""
Write-Host "╔════════════════════════════════════════════════════════════╗" -ForegroundColor $ColorDemo
Write-Host "║  VALIDATION DES LANGUES                                    ║" -ForegroundColor $ColorDemo
Write-Host "╚════════════════════════════════════════════════════════════╝" -ForegroundColor $ColorDemo
Write-Host ""

python scripts/validate_all.py

# Conclusion
Write-Host ""
Write-Host "╔════════════════════════════════════════════════════════════╗" -ForegroundColor $ColorSuccess
Write-Host "║                                                            ║" -ForegroundColor $ColorSuccess
Write-Host "║              ✅ DÉMONSTRATION TERMINÉE ✅                  ║" -ForegroundColor $ColorSuccess
Write-Host "║                                                            ║" -ForegroundColor $ColorSuccess
Write-Host "║  🌍 7 Langues | 35 Keywords | 60+ Builtins               ║" -ForegroundColor $ColorSuccess
Write-Host "║  📦 Zero Dépendances | 🧪 100% Testé                     ║" -ForegroundColor $ColorSuccess
Write-Host "║                                                            ║" -ForegroundColor $ColorSuccess
Write-Host "║  GitHub: github.com/fless-lab/multilang-python            ║" -ForegroundColor $ColorSuccess
Write-Host "║                                                            ║" -ForegroundColor $ColorSuccess
Write-Host "╚════════════════════════════════════════════════════════════╝" -ForegroundColor $ColorSuccess
Write-Host ""
Write-Host "Merci! 🎉" -ForegroundColor $ColorSuccess
Write-Host ""


# Here i (Raouf) state that this script is AI Generated
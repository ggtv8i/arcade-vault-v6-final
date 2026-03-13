@echo off
chcp 65001 >nul
title Arcade Vault
echo ══════════════════════════════════════
echo   🕹️  ARCADE VAULT — Local Server
echo ══════════════════════════════════════
echo.
echo  الرابط: http://localhost:8080/arcade-vault.html
echo  للإيقاف: Ctrl+C
echo.

python --version >nul 2>&1 && (python -m http.server 8080 & goto done)
py --version     >nul 2>&1 && (py -m http.server 8080 & goto done)
node --version   >nul 2>&1 && (npx serve -l 8080 . & goto done)

echo ❌ يرجى تثبيت Python: https://python.org
:done
pause

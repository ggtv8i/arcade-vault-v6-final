#!/bin/bash
echo "══════════════════════════════════════"
echo "  🕹️  ARCADE VAULT — Local Server"
echo "══════════════════════════════════════"
echo ""
echo "  الرابط: http://localhost:8080/arcade-vault.html"
echo "  للإيقاف: Ctrl+C"
echo ""
command -v python3 &>/dev/null && exec python3 -m http.server 8080
command -v python  &>/dev/null && exec python -m http.server 8080
command -v node    &>/dev/null && exec npx serve -l 8080 .
echo "❌ يرجى تثبيت Python من: https://python.org"

#!/bin/bash
echo "[*] Installation de CloudStrike (Pentest Cloud) sur Kali..."

sudo apt update
sudo apt install -y python3 python3-pip

# Installation des dépendances Python
pip3 install -r requirements.txt

# Rendre le script principal exécutable
chmod +x cloudstrike.py

echo "[+] Installation terminée. Utilisez : python3 cloudstrike.py [commande]"
echo ""
echo "Exemples de commande :"
echo "  python3 cloudstrike.py enum --provider aws"
echo "  python3 cloudstrike.py check --provider gcp"
echo "  python3 cloudstrike.py run scripts/aws_misconfig.yaml"

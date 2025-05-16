![image](https://github.com/user-attachments/assets/f8bcece5-3966-4439-9c80-354e1fcb6728)


# ☁️ CloudStrike CLI

CloudStrike est un outil CLI pour Kali Linux qui permet de réaliser des pentests automatisés sur des environnements cloud.

## 🎯 Objectifs

* Réaliser du pentest **automatisé sur des environnements cloud**
* Identifier rapidement les **failles de configuration**, **clés exposées**, **permissions abusives**
* Utiliser des **scénarios YAML** pour décrire des chaînes d'attaque
* Étendre les fonctionnalités avec des modules spécifiques (AWS, Azure, GCP)

## 🧠 Fonctionnalités

| Fonction | Description |
| ----- | ----- |
| `enum` | Enumération passive et active du cloud (clé API, bucket, services ouverts) |
| `check` | Vérifie les failles courantes (S3 public, token, escalade IAM, etc.) |
| `run` | Exécution de scénarios YAML (pentest-as-code) |
| `cloud-ai` | Utilisation d'un moteur IA local pour analyser les configurations |

## 📦 Installation

```bash
git clone https://github.com/servais1983/cloudstrike.git
cd cloudstrike
chmod +x install.sh
./install.sh
```

## 🛠️ Commandes

* `enum --provider aws|gcp|azure` : Enumération cloud passive
* `check --provider` : Analyse de sécurité basique
* `cloud-ai --provider` : Suggestions IA locales
* `run scripts/aws_misconfig.yaml` : Scénario YAML complet

## ✅ Exemple

```bash
python3 cloudstrike.py run scripts/aws_misconfig.yaml
```

## 🔧 Requiert

- Kali Linux
- Python 3.7+
- pip3

## 📝 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 🛡️ Avertissement

Cet outil est destiné uniquement à des fins légitimes de test de sécurité. Assurez-vous d'avoir les autorisations nécessaires avant de l'utiliser sur un environnement cloud. Les auteurs ne sont pas responsables de toute utilisation abusive.

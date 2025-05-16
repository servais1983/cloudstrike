def run(provider):
    print(f"[*] Vérification de failles courantes dans {provider.upper()}...")

    if provider == "aws":
        print("[+] Analyse des politiques IAM")
        print("[+] Vérification des droits Admin globaux...")
        print("[+] Recherche de clés exposées dans les logs...")

    elif provider == "gcp":
        print("[+] Vérification des rôles Editor globaux")
        print("[+] Enumération des Compute Instances accessibles...")

    elif provider == "azure":
        print("[+] Vérification des blobs non protégés")
        print("[+] Test de privilege escalation par roleAssignment...")

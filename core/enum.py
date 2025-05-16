def run(provider):
    print(f"[*] Enumération passive pour {provider.upper()}...")

    if provider == "aws":
        print("[+] Recherche de buckets S3 publics...")
        print("[+] Tentative de récupération des rôles IAM attachés...")
    elif provider == "gcp":
        print("[+] Analyse des projets publics GCP et buckets...")
    elif provider == "azure":
        print("[+] Enumération des blobs et comptes de stockage...")

def run(provider):
    print(f"[*] Analyse AI locale pour {provider.upper()} (mode démo)")
    print("[+] Suggestions :")
    print("- Clé IAM exposée : créez un utilisateur limité avec rotation automatique.")
    print("- Bucket public : restreindre les permissions de lecture/écriture à un rôle IAM.")

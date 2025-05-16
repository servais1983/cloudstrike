import yaml
from core import enum, checker, ai_analyzer

def run_script_yaml(path):
    print(f"[*] Chargement du scénario : {path}")
    with open(path, "r") as f:
        data = yaml.safe_load(f)

    provider = data.get("provider")

    for step in data.get("steps", []):
        step_type = step.get("type")
        if step_type == "enum":
            enum.run(provider)
        elif step_type == "check":
            checker.run(provider)
        elif step_type == "cloud-ai":
            ai_analyzer.run(provider)
        else:
            print(f"[!] Étape inconnue : {step_type}")

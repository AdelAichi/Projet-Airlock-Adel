import requests
from bluetooth_communication import envoyer_message_bluetooth
from serrure_control import verrouiller, deverrouiller
from power_optimization import activer_mode_basse_conso
from prototypage_avance import journaliser_acces

BASE_URL = "https://<ton-url-postman>/serrure/serrure_1"

def valider_acces_utilisateur(user_id):
    response = requests.get(f"{BASE_URL}/open", params={"reservation": user_id, "serrure_1": "on"})
    if response.status_code == 200:
        data = response.json()
        if data.get("access") == "granted":
            return f"Utilisateur {user_id} : Accès autorisé.", True
        else:
            return f"Utilisateur {user_id} : Accès refusé.", False
    else:
        return f"Erreur {response.status_code} : Impossible de vérifier les droits d'accès.", False

if __name__ == "__main__":
    print("=== Communication avec l'API Air Lock Unlock ===")
    user_id = input("Entrez l'ID utilisateur pour vérifier les droits d'accès : ")
    message, acces_autorise = valider_acces_utilisateur(user_id)
    print(message)

    if acces_autorise:
        envoyer_message_bluetooth("Déverrouillage en cours...")
        deverrouiller()
        journaliser_acces(user_id, "Déverrouillé")
    else:
        verrouiller()
        activer_mode_basse_conso()

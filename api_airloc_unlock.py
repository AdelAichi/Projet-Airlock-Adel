import requests

# URL du serveur mock avec les paramètres
url = "https://7b053c83-308c-4225-95a8-3ae0ffd5ca21.mock.pstmn.io/serrure"
params = {'reservation': 1, 'serrure_1': 'on'}  # Utilisation du bon nom de paramètre

# Envoi de la requête GET avec les paramètres
try:
    response = requests.get(url, params=params)  # Envoi de la requête GET
    response.raise_for_status()  # Vérifie si le statut de la réponse est 200 (OK)

    # Vérification du type de contenu dans la réponse
    if response.headers['Content-Type'] == 'application/json':
        print("Réponse du serveur (JSON) :")
        print(response.json())  # Affiche la réponse en JSON
    else:
        print("Réponse du serveur (texte brut) :")
        print(response.text)  # Affiche la réponse brute, au cas où ce n'est pas du JSON

except requests.exceptions.RequestException as e:
    print(f"Erreur de connexion : {e}")

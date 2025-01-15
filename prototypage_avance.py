import csv
from datetime import datetime

def journaliser_acces(user_id, action):
    with open("journal_acces.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([timestamp, user_id, action])
        print(f"Accès journalisé : {timestamp}, Utilisateur {user_id}, Action : {action}")

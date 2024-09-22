import csv
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import pandas as pd

# Öffne die CSV-Datei und lese sie Zeile für Zeile ein
with open('spam_nichtspam_datensatz.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)

    # Speichere alle Zeilen ohne Zeilenumbrüche
    cleaned_rows = []
    for row in reader:
        # Entferne Zeilenumbrüche aus jeder Zelle
        cleaned_row = [cell.replace('\n', ' ').replace('\r', ' ') for cell in row]
        cleaned_rows.append(cleaned_row)

# Schreibe die bereinigten Zeilen in eine neue CSV-Datei
with open('spam_nichtspam_datensatz_output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(cleaned_rows)

# Spam-Words List
spam_words = ["Sex", "sex", "Porno", "porn", "Erotik", "erotisch", "erotic", "nackt", "nude", "Camgirl", "camgirl","MILF","Escort","Dating", "Sexchat", "sex chat",
"Erotikbilder", "Erotic pictures", "XXX","Fetisch"]
file_path = 'spam_nichtspam_datensatz_output.csv'


def check_spam(message: str, spam_words: list) -> bool:
    message_lower = message.lower()
    for word in spam_words:
        if word in message_lower:
            return True
    return False


def process_messages_from_file(file_path: str, spam_words: list):
    spam_count = 0
    non_spam_count = 0

    with open(file_path, 'r', encoding='utf-8') as file:
        messages = file.readlines()

    for i, message in enumerate(messages, start=1):
        if check_spam(message.strip(), spam_words):
            spam_count += 1
            print(f"Das ist Spam: {message.strip()}")
        else:
            non_spam_count += 1

    print(f"Anzahl von Spam-Nachrichten: {spam_count}")
    print(f"Anzahl von Nicht-Spam:  {non_spam_count}")

process_messages_from_file(file_path, spam_words)

# Lade das trainierte Modell und den Vektorisierer
model = joblib.load('spam_modelR.joblib')
vectorizer = joblib.load('vectorizer.joblib')
data = pd.read_csv('spam_nichtspam_datensatz_output.csv')

message = data['message']
message_vectors = vectorizer.transform(message)
predictions = model.predict(message_vectors)
data['prediction'] = predictions
spam_count = data['prediction'].value_counts()

print(f"Model - Anzahl von Spam (1)  und Nicht-Spam (0)  Nachrichten: {spam_count}")

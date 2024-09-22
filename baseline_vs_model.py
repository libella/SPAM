import csv
import joblib
import pandas as pd

#Effektivität des vorhanden Spam-Filter überprüfen.
# CSV-Datei oeffnen und sie Zeile für Zeile einlesen
with open('spam_nichtspam_datensatz.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)

    # alle Zeilen ohne Zeilenumbrüche speichern
    cleaned_rows = []
    for row in reader:
        #  Zeilenumbrüche aus jeder Zelle entfernen
        cleaned_row = [cell.replace('\n', ' ').replace('\r', ' ') for cell in row]
        cleaned_rows.append(cleaned_row)

# bereinigten Zeilen in eine neue CSV-Datei schreiben
with open('spam_nichtspam_datensatz_output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(cleaned_rows)

# Spam-Woerter Liste
spam_words = ["sex", "porno", "porn", "erotik", "erotisch", "erotic", "nackt", "nude", "camgirl","milf","eskort","dating", "escort","sexchat", "sex chat","xxx"]
file_path = 'spam_nichtspam_datensatz_output.csv'

# Nachricht im Kleinbuchstaben konvertiren und über die Liste von Spam-Woerter iterieren um zu checken ob ein Spam-Wort in der Nachricht enthalten ist
def check_spam(message: str, spam_words: list) -> bool:
    message_lower = message.lower()
    for word in spam_words:
        if word in message_lower:
            return True
    return False

# Anzahl der Spam- und Nicht-Spam-Nachrichten zählen
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

# Effektivität des trainierten Modells am selben Datensatz überprüfen.
# das trainierte Modell und den Vektorisierer laden, den csv-Datensatz lesen

model = joblib.load('spam_modelR.joblib')
vectorizer = joblib.load('vectorizer.joblib')
data = pd.read_csv('spam_nichtspam_datensatz_output.csv')

message = data['message']
message_vectors = vectorizer.transform(message)
predictions = model.predict(message_vectors)
data['prediction'] = predictions
spam_count = data['prediction'].value_counts()

print(f"Model - Anzahl von Spam (1)  und Nicht-Spam (0)  Nachrichten: {spam_count}")

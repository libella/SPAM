from sklearn.model_selection import train_test_split #teilt die Daten in Training und Testsets auf
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from imblearn.over_sampling import SMOTE
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
#from google.colab import drive #fuer Colab-Projekt
# Text in Zahlenfeatures konvertieren
from sklearn.feature_extraction.text import TfidfVectorizer
#drive.mount('/content/drive') #fuer Colab-Projekt

# Daten laden
# file_path = '/content/drive/MyDrive/Colab Notebooks/ProjektSpam/spam_nichtspam_datensatz.csv' #fuer Colab-Projekt
file_path = 'spam_nichtspam_datensatz.csv'
df = pd.read_csv(file_path)#fuer Colab-Proje
X = df[['message']]  # Features
y = df['spam']  # Zielvariable

# zur Exploration : Daten in pandas DF laden
pd.set_option('display.max_columns', None)
df = pd.read_csv(file_path)
df.head(3)

print()
print(f"1. Modell trainieren")

# Daten in Trainings- und Testsets aufteilen: 80% zu 20%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f'Trainingssetgröße:{X_train.shape[0]}')
print(f'Testsetgröße:{X_test.shape[0]}')

# Textdaten mit TfidfVectorizer vektorisieren
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train['message'])
X_test_vec = vectorizer.transform(X_test['message'])

# Modell Logistic Regression initialisieren und mit vektorisierten Daten trainieren
model = LogisticRegression()
model.fit(X_train_vec, y_train)

# Vorhersagen machen
y_pred = model.predict(X_test_vec)

# Genauigkeit berechnen
accuracy = accuracy_score(y_test, y_pred)
print(f'Genauigkeit: {accuracy}')

# y_test und y_pred in numerische Labels konvertieren
y_test_numeric = y_test.astype(int)
y_pred_numeric = y_pred.astype(int)

# Precision, Recall, F1 Score ausrechnen (mit numerischen Labels)
precision = precision_score(y_test_numeric, y_pred_numeric)
recall = recall_score(y_test_numeric, y_pred_numeric)
f1 = f1_score(y_test_numeric, y_pred_numeric)
print(f'Precision: {precision}')
print(f'Recall: {recall}')
print(f'F1 Score: {f1}')

# Confusion Matrix (mit numerischen Labels)
cm = confusion_matrix(y_test_numeric, y_pred_numeric)
print(f'Confusion Matrix: {cm}')

# Confusion matrix plotten
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

# Metriken plotten
metrics = {'Metric': ['Accuracy', 'Precision', 'Recall', 'F1 Score'],'Value': [accuracy, precision, recall, f1]}
df = pd.DataFrame(metrics)
sns.barplot(x='Metric', y='Value', hue='Metric', data=df, palette='viridis')
plt.ylim(0, 1.1)
plt.title('Logistic Regression Model Performance Metrics')
for i in range(len(df)):
    # Text auf den Balken setzen
    plt.text(i, df['Value'][i] + 0.02, f'{df["Value"][i]:.2f}', ha='center', va='bottom')
plt.show()

print()
print(f"k-fache Kreuzvalidierung")
k = 5
print(f"Stratified K-Fold Cross Validation auf {k} Folds")
# Textdaten mit TfidfVectorizer vektorisieren
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X['message'])
# vektorisierten Daten an cross_val_score übergeben
scores = cross_val_score(model, X_vec, y, cv=k)
print(f'Cross-Validation Scores: {scores}')
print(f"Mittlere Performanz auf {k} Folds:  {scores.mean()}")
print(f"Standardabweichung der Performanz: {scores.std()}")


print()
print(f"Über-Sampling-Methode - synthetische Beispiele für die Minderheitsklasse ")
# Über-Sampling-Methode SMOTE anwenden, es generiert synthetische Beispiele für die Minderheitsklasse, damit Klassenungleichgewicht ausgeglichen wird.
smote = SMOTE(random_state=42, k_neighbors=5)
X_res, y_res = smote.fit_resample(X_vec, y)

print('Ursprünglicher Datensatz %s' % pd.Series(y).value_counts())
print('Resampelter Datensatz %s' % pd.Series(y_res).value_counts())

print()
print(f"2. Modell  mit Über-Sampling Daten trainieren")
# Über-Sampling Daten in Trainings- und Testsets aufteilen: 80% zu 20%
X_res_train, X_res_test, y_res_train, y_res_test = train_test_split(X_res, y_res, test_size=0.2, random_state=42)
print(f'Über-Sampling Trainingssetgröße:{X_res_train.shape[0]}')
print(f'Über-Sampling Testsetgröße:{X_res_test.shape[0]}')

# Modell initialisieren und  mit Über-Sampling Daten trainieren
modelR = LogisticRegression()
modelR.fit(X_res_train, y_res_train)

# Vorhersagen (Über-Sampling) machen
y_res_pred = modelR.predict(X_res_test)

# Genauigkeit (Über-Sampling) berechnen
accuracyR = accuracy_score(y_res_test, y_res_pred)
print(f'Genauigkeit Über-Sampling: {accuracyR}')

# Über-Sampling y_res_test and y_res_pred in konvertieren
y_res_test_numeric = y_res_test.astype(int)
y_res_pred_numeric = y_res_pred.astype(int)

# Über-Sampling Precision, Recall, F1 Score ausrechnen (mit numerischen Labels )
precisionR = precision_score(y_res_test_numeric, y_res_pred_numeric)
recallR = recall_score(y_res_test_numeric, y_res_pred_numeric)
f1R = f1_score(y_res_test_numeric, y_res_pred_numeric)
print(f'Precision Resample: {precisionR}')
print(f'Recall Resample: {recallR}')
print(f'F1 Score Resample: {f1R}')

# Über-Sampling Confusion Matrix (mit numerischen Labels )
cmR = confusion_matrix(y_res_test_numeric, y_res_pred_numeric)
print(f'Confusion Matrix Resample: {cmR}')


#  Über-Sampling confusion matrix plotten
plt.figure(figsize=(6,4))
sns.heatmap(cmR, annot=True, fmt="d", cmap="Blues", cbar=False,
            xticklabels=['0', '1'],
            yticklabels=['0', '1'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix Resampled')
plt.show()

#  Über-Sampling Metriken plotten
metrics = {'Metric Resampled': ['Accuracy', 'Precision', 'Recall', 'F1 Score'],'Value': [accuracyR, precisionR, recallR, f1R]}
df = pd.DataFrame(metrics)
sns.barplot(x='Metric Resampled', y='Value', hue='Metric Resampled', data=df, palette='viridis')
plt.ylim(0, 1.1)
plt.title('Logistic Regression Model (Resampled) Performance Metrics')
for i in range(len(df)):
    # Text auf den Balken setzen
    plt.text(i, df['Value'][i] + 0.02, f'{df["Value"][i]:.2f}', ha='center', va='bottom')
plt.show()


#Model speichern
file_path = 'spam_modelR.joblib'
joblib.dump(modelR, file_path)
joblib.dump(vectorizer, 'vectorizer.joblib')
print(f"2. Model  ist unter  {file_path} gespeichert")



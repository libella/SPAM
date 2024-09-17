from sklearn.model_selection import train_test_split #teilt die Daten in Training und Testsets auf
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from imblearn.over_sampling import SMOTE
from sklearn.metrics import make_scorer
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
#from google.colab import drive
# Text in Zahlenfeatures konvertieren
from sklearn.feature_extraction.text import TfidfVectorizer
#drive.mount('/content/drive')

# Daten werden geladen
# file_path = '/content/drive/MyDrive/Colab Notebooks/ProjektSpam/spam_nichtspam_datensatz.csv'
file_path = 'spam_nichtspam_datensatz.csv'
df = pd.read_csv(file_path)
X = df[['message']]  # Features
y = df['spam']  # Zielvariable

# zur Exploration : daten in pandas DF laden
pd.set_option('display.max_columns', None)
df = pd.read_csv(file_path)
df.head(3)

# Daten in Trainings- und Testsets aufteilen: 80% zu 20%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f'Trainingssetgröße:{X_train.shape[0]}')
print(f'Testsetgröße:{X_test.shape[0]}')

# Vektorisieren der Textdaten mit TfidfVectorizer
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train['message'])
X_test_vec = vectorizer.transform(X_test['message'])

# Modell initialisieren und trainieren mit vektorisierten Daten
model = LogisticRegression()
model.fit(X_train_vec, y_train)



# Vorhersagen machen
y_pred = model.predict(X_test_vec)


# Genauigkeit berechnen
accuracy = accuracy_score(y_test, y_pred)
print(f'Genauigkeit: {accuracy}')

# Convert y_test and y_pred to numerical labels
y_test_numeric = y_test.astype(int)
y_pred_numeric = y_pred.astype(int)

# Precision, Recall, F1 Score (using numeric labels)
precision = precision_score(y_test_numeric, y_pred_numeric)
recall = recall_score(y_test_numeric, y_pred_numeric)
f1 = f1_score(y_test_numeric, y_pred_numeric)
print(f'Precision: {precision}')
print(f'Recall: {recall}')
print(f'F1 Score: {f1}')

# Confusion Matrix (using numeric labels)
cm = confusion_matrix(y_test_numeric, y_pred_numeric)
print(f'Confusion Matrix: {cm}')


# Plot confusion matrix
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

metrics = {'Metric': ['Accuracy', 'Precision', 'Recall', 'F1 Score'],'Value': [accuracy, precision, recall, f1]}
df = pd.DataFrame(metrics)
sns.barplot(x='Metric', y='Value', hue='Metric', data=df, palette='viridis')
plt.ylim(0, 1.1)
plt.title('Logistic Regression Model Performance Metrics')
for i in range(len(df)):
    # Text auf den Balken setzen
    plt.text(i, df['Value'][i] + 0.02, f'{df["Value"][i]:.2f}', ha='center', va='bottom')
plt.show()


# k-fache Kreuzvalidierung
k = 3
print(f"Stratified K-Fold Cross Validation auf {k} Folds")
# Vektorisieren der Textdaten mit TfidfVectorizer
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X['message']) # Vectorize the entire dataset
scores = cross_val_score(model, X_vec, y, cv=k) # Pass the vectorized data to cross_val_score
print(f'Cross-Validation Scores: {scores}')
print(f"Mittlere Performanz auf {k} Folds:  {scores.mean()}")
print(f"Standardabweichung der Performanz: {scores.std()}")


# Erstelle den SMOTE OverSampler
smote = SMOTE(random_state=42, k_neighbors=5) # Set k_neighbors to 5
X_res, y_res = smote.fit_resample(X_vec, y)

print('Original dataset shape %s' % pd.Series(y).value_counts())
print('Resampled dataset shape %s' % pd.Series(y_res).value_counts())

# OverSampler Daten in Trainings- und Testsets aufteilen: 80% zu 20%
X_res_train, X_res_test, y_res_train, y_res_test = train_test_split(X_res, y_res, test_size=0.2, random_state=42)
print(f'OverSampler Trainingssetgröße:{X_res_train.shape[0]}')
print(f'OverSampler Testsetgröße:{X_res_test.shape[0]}')

# Modell initialisieren und trainieren mit OverSampler Daten
modelR = LogisticRegression()
modelR.fit(X_res_train, y_res_train)

# OverSampler Vorhersagen machen
y_res_pred = modelR.predict(X_res_test)


# OverSampler Genauigkeit berechnen
accuracy = accuracy_score(y_res_test, y_res_pred)
print(f'Genauigkeit Resample: {accuracy}')

# OverSampler Convert y_res_test and y_res_pred to numerical labels
y_res_test_numeric = y_res_test.astype(int)
y_res_pred_numeric = y_res_pred.astype(int)

# OverSampler Precision, Recall, F1 Score (using numeric labels)
precisionR = precision_score(y_res_test_numeric, y_res_pred_numeric)
recallR = recall_score(y_res_test_numeric, y_res_pred_numeric)
f1R = f1_score(y_res_test_numeric, y_res_pred_numeric)
print(f'Precision Resample: {precisionR}')
print(f'Recall Resample: {recallR}')
print(f'F1 Score Resample: {f1R}')

# OverSampler Confusion Matrix (using numeric labels)
cmR = confusion_matrix(y_res_test_numeric, y_res_pred_numeric)
print(f'Confusion Matrix Resample: {cmR}')


# Plot OverSampler confusion matrix
sns.heatmap(cmR, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

#Model speichern
file_path = 'spam_modelR.joblib'
joblib.dump(modelR, file_path)
print(f"Model saved successfully at {file_path}")
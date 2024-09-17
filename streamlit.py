import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Funktion zum Laden des Modells
def load_modelR():
    with open('spam_modelR.joblib', 'rb') as file:
        modelR = joblib.load(file)
    return modelR

modelR = load_modelR()

# Nutzer-Eingaben
st.title('Spam-Projekt, IKT-SS24')
st.subheader('Irina Ukhanova')

st.subheader('Ist diese Nachricht Spam oder nicht?')
st.markdown('Probieren Sie dieses ML-Modell aus, um zu prüfen, ob die Nachricht auf den P4G-Portalen als Spam markiert werden sollte.')
def user_input():
	message = st.text_area("Geben Sie hier die Nachricht an (nicht mehr als 1000 Zeichen):", max_chars=1000)
	data = {
        'message': message
	}
	return np.array(list(data.values()))
input_data = user_input()

# Vorhersage
prediction = modelR.predict(input_data)

# Vorhersage-Ergebnis anzeigen
st.write(f'Die Nachricht ist: **{prediction[0]}**')


import streamlit as st
import joblib

# Lade das trainierte Modell und den Vektorisierer
model = joblib.load('spam_modelR.joblib')
vectorizer = joblib.load('vectorizer.joblib')

# Titel und Beschreibung der App
st.title('Spam-Projekt, IKT-SS24')
st.subheader('Irina Ukhanova')

st.subheader('Ist diese Nachricht Spam oder nicht?')
st.write('Probieren Sie dieses ML-Modell aus, um zu prüfen, ob die Nachricht auf den P4G-Portalen als Spam markiert werden sollte.')

# Text-Eingabe vom Nutzer
input_text = st.text_area('Nachricht eingeben:')

if st.button('Überprüfen'):
    if input_text:
        # Verarbeite die Nutzereingabe
        input_vector = vectorizer.transform([input_text])
        
        # Vorhersage
        prediction = model.predict(input_vector)
        
        # Zeige das Ergebnis an
        if prediction == 1:
            st.error('Diese Nachricht ist **Spam**.')
        else:
            st.success('Diese Nachricht ist **kein Spam**.')
    else:
        st.warning('Bitte geben Sie eine Nachricht ein.')












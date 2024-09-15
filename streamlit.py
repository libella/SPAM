import streamlit as st
import pandas as pd
import numpy as np
import joblib
from prediction import predict


st.title('Spam-Projekt, IKT-SS24')
st.subheader('Irina Ukhanova')

st.subheader('Ist diese Nachricht Spam oder nicht?')
st.markdown('Probieren Sie dieses ML-Modell aus, um zu prüfen, ob die Nachricht auf den P4G-Portalen als Spam markiert werden sollte.')
with st.form("my_form"):
	email = st.text_input("E-Mail")
	txt = st.text_area("Geben Sie hier die Nachricht an (nicht mehr als 1000 Zeichen):", max_chars=1000)
	if st.form_submit_button("Spam oder nicht?"):
		result = predict(np.array([[email, txt]]))
		st.text(result[0])
	#submitted = st.form_submit_button("Spam oder nicht?")
	#if submitted:
		#st.write ("Prüfung läuft")
import joblib
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

message = joblib.load ('spam_modelR.joblib')

def data_preprocessing(data):
    data = data.copy()
    df = pd.DataFrame()
    # Vektorisieren der Textdaten mit TfidfVectorizer
    vectorizer = TfidfVectorizer()
    df['message'] = vectorizer.fit_transform(data['message'])
    return df

import joblib


def predict(data):
    model = joblib.load("spam_model.sav")
    return model.predict(data)


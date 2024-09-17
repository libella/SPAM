import joblib

def predict(data):
    modelR = joblib.load('spam_modelR.joblib')
    return modelR.predict(data)


#def predict(data):
    #result = modelR.predict(data)
    #final_result = "Spam" if result == 1 else "Nicht Spam"
    #return final_result


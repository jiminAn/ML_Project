def prediction(tweet):
    ## warning off
    import warnings
    warnings.filterwarnings(action='ignore') # default = off

    ## model load
    model_path = "./"
    import pickle   # or joblib
    loaded_vector = pickle.load(open(model_path+"vector002-2021-11-13-09-F1-077018.pkl", "rb"))
    loaded_model = pickle.load(open(model_path+"model002-2021-11-13-09-F1-077018.pkl", "rb"))

    ## using model
    vec = loaded_vector
    X_test_vector = vec.transform([tweet])  # Generate TFIDF vector

    ## Prediction
    res = loaded_model.predict(X_test_vector.todense()) # input is string

    print(f"{tweet}: {res}")

if __name__ == '__main__':
    prediction("It's raining")
    prediction("There's a fire over there. it's dangerous..")


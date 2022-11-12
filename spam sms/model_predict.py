def predict_spam(sample_message):
    import nltk
    import re
    nltk.download('stopwords')
    nltk.download('wordnet')
    from nltk.corpus import stopwords
    from nltk.stem import WordNetLemmatizer
    import joblib
    tfidf = joblib.load('fit_transformer.joblib')
    wnl = WordNetLemmatizer()

    rf = joblib.load('sms_spam_classifier_model.sav')
    sample_message = re.sub(pattern='[^a-zA-Z]',repl=' ', string = sample_message)
    sample_message = sample_message.lower()
    sample_message_words = sample_message.split()
    sample_message_words = [word for word in sample_message_words if not word in set(stopwords.words('english'))]
    final_message = [wnl.lemmatize(word) for word in sample_message_words]
    final_message = ' '.join(final_message)


    temp = tfidf.transform([final_message]).toarray()
    return rf.predict(temp)


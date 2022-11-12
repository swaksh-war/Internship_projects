def preprocess(message):
    import nltk
    nltk.download('stopwords')
    from nltk.corpus import stopwords
    from nltk.stem.porter import PorterStemmer
    import re
    from sklearn.feature_extraction.text import CountVectorizer
    ps = PorterStemmer()
    corpus = []
    review = re.sub('[^a-zA-Z]', ' ', message)
    review = review.lower()
    review = review.split()
    
    review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
    review = ' '.join(review)
    corpus.append(review)
    cv = CountVectorizer(max_features=5000, ngram_range = (1,3))
    x = cv.fit_transform(corpus).toarray()
    return x
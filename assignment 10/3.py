from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

texts = [
    "Output is certain",
    "Exact output is unknown",
    "Relationships between inputs are known"
]

bow = CountVectorizer()
bow_fit = bow.fit_transform(texts)
print("Bag of Words:", bow.get_feature_names_out())
tfidf = TfidfVectorizer()
tfidf_fit = tfidf.fit_transform(texts)
names = tfidf.get_feature_names_out()
for i in range(len(texts)):
    scores = tfidf_fit[i].toarray()[0]
    pairs = list(zip(names, scores))
    top = sorted(pairs, key=lambda x: x[1], reverse=True)[:3]
    print("Top 3 in text", i+1, ":", [x[0] for x in top])

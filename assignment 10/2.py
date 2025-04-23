from nltk.stem import PorterStemmer, WordNetLemmatizer
nltk.download('wordnet')
only_alpha = re.findall(r'\b[a-zA-Z]+\b', text)
filtered_alpha = [w for w in only_alpha if w not in stop]

stem = PorterStemmer()
lemma = WordNetLemmatizer()
stem_words = [stem.stem(w) for w in filtered_alpha]
lemma_words = [lemma.lemmatize(w) for w in filtered_alpha]
print( filtered_alpha)
print( stem_words)
print( lemma_words)

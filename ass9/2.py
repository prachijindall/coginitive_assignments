from nltk.stem import PorterStemmer, LancasterStemmer, WordNetLemmatizer 
nltk.download('wordnet')
porter = PorterStemmer()
lancaster = LancasterStemmer()
lemmatizer = WordNetLemmatizer()
porter_stems = [porter.stem(word) for word in filtered_words]
lancaster_stems = [lancaster.stem(word) for word in filtered_words]
lemmatized = [lemmatizer.lemmatize(word) for word in filtered_words]
print( porter_stems)
print( lancaster_stems)
print(lemmatized)

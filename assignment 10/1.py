import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
nltk.download('punkt')
nltk.download('stopwords')
text = "A deterministic system would have to return a single answer based on the evidence, or no answer if there were a condition of uncertainty"
text = text.lower()
text = re.sub(r'[^\w\s]', '', text)
sentences = sent_tokenize(text)
tokens_nltk = word_tokenize(text)
tokens_split = text.split()

stop = set(stopwords.words("english"))
filtered = [w for w in tokens_nltk if w not in stop]

freq = FreqDist(filtered)

print( tokens_split)
print( tokens_nltk)
print( filtered)
freq.plot()

import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist

nltk.download('punkt')
nltk.download('stopwords')
text = "In a probabilistic system, there may be avariety of answers, depending on circumstances or context and the confidence level or probability based on the system’s current knowledge"

text_lower = text.lower()
text_clean = text_lower.translate(str.maketrans('', '', string.punctuation))
word_tokens = word_tokenize(text_clean)
sent_tokens = sent_tokenize(text)
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in word_tokens if word not in stop_words]
freq_dist = FreqDist(filtered_words)

print( sent_tokens)
print( filtered_words)
freq_dist.plot()

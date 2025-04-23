from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

a = "Focuses on building systems that replace human intelligence for automating tasks and decision-making."
b = "Focuses on building systems that augment human intelligence, helping humans make better decisions."
a = a.lower()
b = b.lower()
a_tokens = set(re.findall(r'\b[a-z]+\b', a))
b_tokens = set(re.findall(r'\b[a-z]+\b', b))
inter = a_tokens & b_tokens
union = a_tokens | b_tokens
jaccard = len(inter) / len(union)
print( jaccard)
vec = TfidfVectorizer()
cos = cosine_similarity(vec.fit_transform([a, b]))
print( cos[0][1])

import re
long_words = re.findall(r'\b\w{6,}\b', text)
numbers = re.findall(r'\d+', text)

capital_words = re.findall(r'\b[A-Z][a-z]*\b', text)
alpha_words = re.findall(r'\b[a-zA-Z]+\b', text)
vowel_words = [word for word in alpha_words if word.lower().startswith(('a', 'e', 'i', 'o', 'u'))]

print( long_words)
print( numbers)
print( capital_words)
print( alpha_words)
print(vowel_words)

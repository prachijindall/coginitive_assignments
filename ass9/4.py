def custom_tokenizer(text):
    text = re.sub(r'[^\w\s\'\-\.]', '', text)  
    tokens = re.findall(r"\b(?:\d+\.\d+|\w+(?:-\w+)*|'[\w]+|\w+)\b", text)
    return tokens
sample_text = "Email me at examplee.user@example.com or visit https://example.com. Call me at +91 9876543210 or 123-456-7890."

cleaned = re.sub(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', '<EMAIL>', sample_text)
cleaned = re.sub(r'https?://\S+', '<URL>', cleaned)
cleaned = re.sub(r'(\+91\s?\d{10}|\d{3}-\d{3}-\d{4})', '<PHONE>', cleaned)

print( custom_tokenizer(text))
print( cleaned)

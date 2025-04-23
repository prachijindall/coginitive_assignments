from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt

reviews = [
    "Works autonomously to solve problems.",
    "Collaborates with humans to assist in problem-solving.",
    "AI Powered chatbots like Siri, Alexa."
]
for r in reviews:
    blob = TextBlob(r)
    print(r)
    print("Polarity:", blob.sentiment.polarity)
    print("Subjectivity:", blob.sentiment.subjectivity)
    if blob.sentiment.polarity > 0:
        print("Positive")
    elif blob.sentiment.polarity < 0:
        print("Negative")
    else:
        print("Neutral")

positive = " ".join([r for r in reviews if TextBlob(r).sentiment.polarity > 0])
cloud = WordCloud().generate(positive)
plt.imshow(cloud, interpolation="bilinear")
plt.axis("off")
plt.show()

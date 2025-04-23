from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense

text = "Decision-support systems in industries like healthcare, finance, and education."

token = Tokenizer()
token.fit_on_texts([text])
seq = token.texts_to_sequences([text])[0]
data = []
for i in range(1, len(seq)):
    data.append(seq[:i+1])

data = pad_sequences(data)
model = Sequential()
model.add(Embedding(len(token.word_index)+1, 10, input_length=data.shape[1]-1))
model.add(LSTM(50))
model.add(Dense(len(token.word_index)+1, activation="softmax"))
model.compile(loss="sparse_categorical_crossentropy", optimizer="adam")
model.fit(data[:,:-1], data[:,-1], epochs=200, verbose=0)
import numpy as np

def generate(seed, count=3):
    for _ in range(count):
        seq = token.texts_to_sequences([seed])[0]
        seq = pad_sequences([seq], maxlen=data.shape[1]-1)
        pred = model.predict(seq, verbose=0)
        word = token.index_word[np.argmax(pred)]
        seed += " " + word
    print( seed)

generate("AI")

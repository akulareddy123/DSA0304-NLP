import nltk
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
words = [
    "playing",
    "played",
    "plays",
    "running",
    "runner",
    "studies",
    "studying",
    "connected"
]
print("Porter Stemmer")
print("--------------")
print("Word\t\tStem")
print("--------------")
for word in words:
    stem = stemmer.stem(word)
    print(word, "\t\t", stem)
import nltk
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
words = [
    "playing",
    "played",
    "plays",
    "running",
    "studies",
    "studying",
    "cats",
    "dogs"
]
print("Morphological Analysis using NLTK")
print("----------------------------------")
print("Word\t\tStem")
print("----------------------------------")
for word in words:
    stem = stemmer.stem(word)
    print(word, "\t\t", stem)
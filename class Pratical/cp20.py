from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "Python is a programming language",
    "Natural language processing uses Python",
    "Football is a popular sport"
]

query = input("Enter search query: ")

vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(documents + [query])

scores = cosine_similarity(tfidf[-1], tfidf[:-1]).flatten()

ranked = scores.argsort()[::-1]

print("\nRanked Documents:")

for i in ranked:
    print(documents[i], "-> Score:", round(scores[i], 3))
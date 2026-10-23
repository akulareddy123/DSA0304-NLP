import nltk
from nltk.corpus import wordnet

nltk.download('wordnet')
nltk.download('omw-1.4')

word = "book"
synsets = wordnet.synsets(word)

for syn in synsets[:5]:
    print("Synset:", syn.name())
    print("Meaning:", syn.definition())
    print()
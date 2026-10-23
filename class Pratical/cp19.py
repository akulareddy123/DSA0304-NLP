import nltk
from nltk.wsd import lesk
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)
sentence = "I deposited money in the bank"
word = "bank"
sense = lesk(sentence.split(), word, pos='n')
if sense:
    print("Sentence:", sentence)
    print("Target Word:", word)
    print("Meaning:", sense.definition())
else:
    print("No meaning found")
import nltk
from nltk import RegexpParser
from nltk.corpus import wordnet

# Download required data
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('wordnet')

# Input sentence
sentence = "The intelligent student reads a book"

# Tokenization and POS tagging
words = nltk.word_tokenize(sentence)
tags = nltk.pos_tag(words)

# Grammar for noun phrases
grammar = "NP: {<DT>?<JJ>*<NN.*>+}"

parser = RegexpParser(grammar)
tree = parser.parse(tags)

print("Noun Phrases and Meanings:")

for subtree in tree.subtrees():
    if subtree.label() == 'NP':
        phrase = " ".join(word for word, tag in subtree.leaves())
        print("\nNoun Phrase:", phrase)

        for word, tag in subtree.leaves():
            if tag.startswith('NN'):
                meanings = wordnet.synsets(word)
                if meanings:
                    print(word, ":", meanings[0].definition())
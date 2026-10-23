import nltk

grammar = nltk.CFG.fromstring("""
S -> NS VS | NP VP
NS -> 'he' | 'she'
VS -> 'runs' | 'eats'
NP -> 'they' | 'we'
VP -> 'run' | 'eat'
""")

parser = nltk.ChartParser(grammar)

sentences = ["he runs", "they run", "he run", "they runs"]

for sentence in sentences:
    words = sentence.split()
    if list(parser.parse(words)):
        print(sentence, ": Correct Agreement")
    else:
        print(sentence, ": Incorrect Agreement")
import nltk

grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> 'the' 'boy' | 'the' 'girl'
VP -> 'runs' | 'eats'
""")

parser = nltk.EarleyChartParser(grammar)
sentence = "the girl eats".split()

for tree in parser.parse(sentence):
    print(tree)
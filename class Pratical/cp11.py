import nltk
grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> 'the' 'boy' | 'the' 'girl'
VP -> 'runs' | 'eats'
""")
parser = nltk.TopDownChartParser(grammar)
sentence = "the boy runs".split()
for tree in parser.parse(sentence):
    print(tree)
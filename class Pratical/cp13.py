import nltk

grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> 'John' | 'Mary'
VP -> V NP
V -> 'likes'
""")

parser = nltk.ChartParser(grammar)
sentence = "John likes Mary".split()

for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
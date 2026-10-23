import nltk

grammar = nltk.PCFG.fromstring("""
S -> NP VP [1.0]
NP -> 'John' [0.5] | 'Mary' [0.5]
VP -> 'runs' [0.6] | 'sleeps' [0.4]
""")

parser = nltk.ViterbiParser(grammar)
sentence = "John runs".split()

for tree in parser.parse(sentence):
    print(tree)
    print("Probability:", tree.prob())
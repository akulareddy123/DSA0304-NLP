import re

text = "Ravi is a student. He studies Python. Ravi likes programming."

words = text.split()
nouns = ["Ravi", "student", "Python", "programming"]

print("Reference Resolution")
print("--------------------")

for word in words:
    if word.lower().strip(".,") in ["he", "she", "it", "they"]:
        print(word, "refers to", nouns[0])
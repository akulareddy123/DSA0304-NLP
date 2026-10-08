def pluralize(word):
    state = 0
    if word.endswith(("s", "x", "z", "ch", "sh")):
        state = 1
        return word + "es"
    elif word.endswith("y") and len(word) > 1 and word[-2] not in "aeiou":
        state = 2
        return word[:-1] + "ies"
    else:
        state = 3
        return word + "s"
words = ["cat", "box", "bus", "baby", "dish", "book"]
print("Singular\tPlural")
for word in words:
    plural = pluralize(word)
    print(word, "\t\t", plural)
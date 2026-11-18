import re

text = input("Enter a paragraph: ")

sentences = re.split(r'[.!?]+', text)

sentences = [s.strip().lower() for s in sentences if s.strip()]

print("\nCoherence Evaluation")

total = 0
count = 0

for i in range(len(sentences) - 1):
    words1 = set(sentences[i].split())
    words2 = set(sentences[i + 1].split())

    common = words1.intersection(words2)

    score = len(common) / max(len(words1), len(words2))

    print("Similarity:", round(score, 2))

    total += score
    count += 1

if count > 0:
    average = total / count
    print("Average Coherence Score:", round(average, 2))

    if average >= 0.2:
        print("Text is Coherent")
    else:
        print("Text has Low Coherence")
else:
    print("Enter at least two sentences")
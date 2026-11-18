def dialog_act(sentence):
    sentence = sentence.lower()

    if "hello" in sentence or "hi" in sentence:
        return "Greeting"

    elif sentence.endswith("?"):
        return "Question"

    elif "please" in sentence:
        return "Request"

    elif "thank" in sentence:
        return "Thanking"

    elif "bye" in sentence:
        return "Goodbye"

    else:
        return "Statement"


print("Dialog Act Recognition")

sentence = input("Enter a sentence: ")

result = dialog_act(sentence)

print("Dialog Act:", result)
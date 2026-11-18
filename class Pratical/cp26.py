from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load translation model
model_name = "Helsinki-NLP/opus-mt-en-fr"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Get English input
text = input("Enter English sentence: ")

# Tokenization
inputs = tokenizer(text, return_tensors="pt")

# Translate text
translated = model.generate(**inputs)

# Decode translation
result = tokenizer.decode(translated[0], skip_special_tokens=True)

print("French Translation:", result)
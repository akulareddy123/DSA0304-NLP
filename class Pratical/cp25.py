from openai import OpenAI

# Create OpenAI client
client = OpenAI(api_key="YOUR_API_KEY")

# Get prompt from user
prompt = input("Enter your prompt: ")

# Generate text
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

# Display generated text
print("\nGenerated Text:")
print(response.choices[0].message.content)
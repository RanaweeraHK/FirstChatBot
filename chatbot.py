import openai

openai.api_key ="your-api-key"

def chat_with_bot(prompt):
    response = openai.ChatCompletion.create(
      model = "gpt-3.5-turbo",
      messages = [{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            break
        response = chat_with_bot(user_input)
        print("ChatBot: ", response)

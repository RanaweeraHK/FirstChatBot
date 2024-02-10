import openai

openai.api_key =

def chat_with_bot(prompt):
    response = openai.Completion.create(
      response = [{}]
    )
    return response.choices[0].text.strip()
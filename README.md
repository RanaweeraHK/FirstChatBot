
# ChatBot using OpenAI GPT-3.5

Welcome to the ChatBot project! This repository contains a simple implementation of a conversational chatbot using OpenAI's GPT-3.5 model. The bot can engage in text-based conversations, responding to user prompts with relevant and coherent messages.

## Features

- Interactive conversational interface.
- Uses OpenAI's GPT-3.5 model for generating responses.
- Simple command-line interface.
- Graceful exit on user command.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Python 3.6 or higher
- OpenAI Python library

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/RanaweeraHK/First-Chat-Bot.git
   cd First-Chat-Bot
   ```

2. **Install dependencies**:
   It's recommended to use a virtual environment to manage dependencies. Run the following commands:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install openai
   ```

3. **Set up OpenAI API key**:
   Replace `"your-api-key"` in the `chat_with_bot` function with your actual OpenAI API key. You can obtain an API key by signing up at [OpenAI](https://beta.openai.com/signup/).

## Usage

1. **Run the chatbot**:
   ```sh
   python chatbot.py
   ```

2. **Interact with the bot**:
   Type your messages in the command line interface. To exit the chat, type `exit`, `quit`, or `bye`.

## Example

Here's a simple example of how the chat might look:

```sh
You: Hello, how are you?
ChatBot: I'm just a bot, but I'm here to help! How can I assist you today?
You: Tell me a joke.
ChatBot: Why don't scientists trust atoms? Because they make up everything!
You: exit
```

Able to read the Medium article using this link:
(https://medium.com/@ranaweerahk/from-idea-to-reality-crafting-my-first-chatbot-07ad1912b365)

import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey!"]
    ],
    [
        r"what is your name?",
        ["My name is SimpleBot.", "I'm SimpleBot, nice to meet you!"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm fine, how about you?"]
    ],
    [
        r"quit",
        ["Bye, take care!", "It was nice talking to you. Goodbye!"]
    ],
]

def get_response(user_message):
    # Your chatbot logic here
    return "This is a response from the chatbot"

def chatbot():
    print("Hi! I'm SimpleBot. How can I help you today?")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    nltk.download('punkt')
    chatbot()

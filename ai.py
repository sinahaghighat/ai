import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses for the chatbot
pairs = [
    ['hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']],
    ['how are you?', ['I am doing well, thank you!', 'I\'m good, thanks for asking. How about you?']],
    ['(what is your name|who are you)', ['I am a chatbot created with Python NLTK. You can call me ChatPy!']],
    ['(quit|exit)', ['Bye!', 'Goodbye!', 'See you later!']],
    ['(.*)', ['That\'s interesting.', 'Tell me more.']]
]

# Create a Chat object
chatbot = Chat(pairs, reflections)

# Start chatting
print("Welcome to ChatPy! How can I help you today?")
while True:
    user_input = input("You: ")
    response = chatbot.respond(user_input)
    print("ChatPy:", response)

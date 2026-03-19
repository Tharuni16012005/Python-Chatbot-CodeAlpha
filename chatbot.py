import random
import datetime

# Greeting responses
greetings = ["hello", "hi", "hey", "good morning", "good evening"]
greeting_responses = [
    "Hello! How can I help you today?",
    "Hi there! What can I do for you?",
    "Hey! Nice to talk to you.",
    "Hello! Ask me anything."
]

# Questions and responses
responses = {
    "how are you": [
        "I am doing great!",
        "I'm just a bot, but I'm doing fine.",
        "All good here. How about you?"
    ],
    "your name": [
        "I am CodeAlpha ChatBot.",
        "You can call me PythonBot.",
        "I'm your friendly Python chatbot."
    ],
    "what can you do": [
        "I can answer simple questions and chat with you.",
        "I can tell time, greet you, and have a small conversation.",
        "I'm here to practice Python chatbot skills."
    ],
    "who created you": [
        "I was created using Python.",
        "A Python programmer developed me.",
        "I was built as a CodeAlpha internship project."
    ],
    "python": [
        "Python is a popular programming language.",
        "Python is widely used for AI, web development, and data science.",
        "Python is simple and powerful."
    ]
}

# Unknown response list
unknown_responses = [
    "Sorry, I didn't understand that.",
    "Can you rephrase your question?",
    "I'm still learning. Please ask something else.",
    "Interesting question! I don't know the answer yet."
]

# Function to get greeting response
def greet(user_input):
    for word in user_input.split():
        if word in greetings:
            return random.choice(greeting_responses)
    return None

# Function to get time
def get_time():
    now = datetime.datetime.now()
    return "Current time is " + now.strftime("%H:%M:%S")

# Function to get date
def get_date():
    today = datetime.date.today()
    return "Today's date is " + today.strftime("%B %d, %Y")

# Function to get chatbot response
def get_response(user_input):

    # Greeting detection
    greeting = greet(user_input)
    if greeting:
        return greeting

    # Time query
    if "time" in user_input:
        return get_time()

    # Date query
    if "date" in user_input:
        return get_date()

    # Check predefined responses
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    # Unknown response
    return random.choice(unknown_responses)

# Chatbot main program
def chatbot():

    print("=================================")
    print("      Python ChatBot")
    print(" Type 'exit', 'bye', or 'quit' to stop ")
    print("=================================")

    while True:

        user_input = input("\nYou: ").lower()

        if user_input in ["exit", "bye", "quit"]:
            print("Bot: Goodbye! Have a nice day.")
            break

        response = get_response(user_input)
        print("Bot:", response)

# Run chatbot
chatbot()

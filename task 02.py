# Import necessary libraries
import random

# Define a set of responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm good, thank you!", "Doing great, and you?", "I'm just a bot, but I'm fine!"],
    "what is your name": ["I'm a chatbot!", "I don't have a name, but I'm here to help!"],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
}

# Function to get a response based on the user's input
def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return "I'm not sure I understand. Can you rephrase that?"

# Main function to run the chatbot
def chatbot():
    print("Hello! I'm a chatbot. Type 'hi' to continue the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "hi":
            print("Chatbot: hello!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
if _name_ == "_main_":
    chatbot()
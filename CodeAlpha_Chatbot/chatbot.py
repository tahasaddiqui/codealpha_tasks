# Basic Chatbot - CodeAlpha Internship
# Author: Muhammad Taha Saddiqui

def chatbot():
    print("🤖 Hello! I’m AlphaBot — your friendly chatbot.")
    print("Type 'bye' anytime to end the chat.\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["hi", "hello", "hey"]:
            print("AlphaBot: Hi there! How are you doing?")
        elif user_input in ["i'm fine", "i am fine", "good", "great"]:
            print("AlphaBot: That’s awesome to hear!")
        elif user_input in ["how are you", "how are you?"]:
            print("AlphaBot: I’m just a bunch of code, but I’m doing great!")
        elif user_input in ["bye", "exit", "quit"]:
            print("AlphaBot: Goodbye! Have a great day 👋")
            break
        elif user_input == "":
            print("AlphaBot: Don’t be shy, say something!")
        else:
            print("AlphaBot: I’m not sure I understand that, but I’m learning every day!")

# Run chatbot
if __name__ == "__main__":
    chatbot()

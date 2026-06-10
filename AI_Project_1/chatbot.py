print("🤖 ChatBot Started!")
print("Type 'bye' to exit")

while True:
    user = input("You: ").lower().strip()

    if user == "hello" or user == "hi":
        print("Bot: Hello! How are you?")

    elif user == "how are you":
        print("Bot: I am fine. Thanks for asking!")

    elif user == "what is your name":
        print("Bot: I am a Rule-Based AI Chatbot.")

    elif user == "good morning":
         print("Bot: Good Morning!")

    elif user == "thank you":
        print("Bot: You're welcome!")

    elif user == "who created you":
        print("Bot: I was created by Josna.")

    elif user == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand.")

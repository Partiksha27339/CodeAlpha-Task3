def chatbot_game(user_input):
    text = user_input.lower()
    if "hello" in text or "hi" in text:
        return "HELLO! "
    elif "how are you" in text:
        return "I'm fine."
    elif "bye" in text or "goodbye" in text:
        return "Goodbye! It was nice talking with you."
    elif "thanks" in text or "thank you" in text:
        return "You're welcome!"
    else:
        return "Sorry, I don't understand. Can you please repeat it again"
print("Chatbot: Hello! Type 'bye' to exit.")
while True:
    user = input("You: ")
    if user.lower() in ("bye", "goodbye"):
        print("Chatbot:", chatbot_game(user))
        break
    print("Chatbot:", chatbot_game(user))
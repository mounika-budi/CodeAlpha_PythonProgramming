def get_chatbot_response(user_input):
    clean_input = user_input.strip().lower()

    if clean_input in ["hello", "hi", "hey", "greetings"]:
        return "Hello! How can I assist you today?"
    elif "how are you" in clean_input:
        return "I'm doing well, thank you for asking! How are you?"
    elif "name" in clean_input:
        return "I am a simple rule-based Python chatbot created for CodeAlpha."
    elif "help" in clean_input:
        return "I can answer basic greetings, chat, or wish you goodbye! Type 'bye' to exit."
    elif clean_input in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't quite understand that. Type 'help' to see what I can do!"

def run_chatbot():
    print("=========================================")
    print(" Welcome to CodeAlpha Rule-Based Chatbot ")
    print(" Type 'bye' or 'exit' to stop the chat.  ")
    print("=========================================\n")

    while True:
        user_text = input("You: ")
        if not user_text.strip():
            continue

        response = get_chatbot_response(user_text)
        print(f"Bot: {response}\n")

        if user_text.strip().lower() in ["bye", "goodbye", "exit", "quit"]:
            break

if __name__ == "__main__":
    run_chatbot()
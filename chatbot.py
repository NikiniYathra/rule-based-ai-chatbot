"""
Project 1: Rule-Based AI Chatbot
DecodeLabs Artificial Intelligence Industrial Training Kit

A simple rule-based chatbot that uses:
- Continuous input loop
- Input sanitization
- Dictionary-based responses
- Exit commands
- Fallback response
"""

def sanitize_input(user_input):
    """Convert input to lowercase and remove extra spaces."""
    return user_input.lower().strip()


def get_response(user_input, responses):
    """Return chatbot response using dictionary lookup."""
    return responses.get(
        user_input,
        "Sorry, I don't understand that yet. Try asking something else."
    )


def run_chatbot():
    responses = {
        "hello": "Hi there! How can I help you?",
        "hi": "Hello! Nice to meet you.",
        "how are you": "I'm doing great. Thanks for asking!",
        "what is your name": "I am a simple rule-based AI chatbot.",
        "help": "You can say hello, ask my name, ask how I am, or type exit to quit.",
        "thank you": "You're welcome!",
        "thanks": "No problem!",
        "what can you do": "I can respond to predefined inputs using rule-based logic."
    }

    exit_commands = ["exit", "bye", "quit", "goodbye"]

    print("Rule-Based AI Chatbot")
    print("Type 'help' to see what you can ask.")
    print("Type 'exit' to end the chat.\n")

    while True:
        raw_input = input("You: ")
        user_input = sanitize_input(raw_input)

        if user_input in exit_commands:
            print("Bot: Goodbye! Have a great day.")
            break

        response = get_response(user_input, responses)
        print("Bot:", response)


if __name__ == "__main__":
    run_chatbot()

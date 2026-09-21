
BOT_NAME = "Byte"

# Layer 1: Exact-match Knowledge Base

responses = {
    "hello": f"Hi there! I'm {BOT_NAME}. How can I help you today?",
    "hi": f"Hey! {BOT_NAME} here, ready to chat.",
    "hey": "Hey! What's up?",
    "how are you": "Running at 100% logic capacity. Thanks for asking!",
    "what is your name": f"I'm {BOT_NAME}, a rule-based chatbot built for help.",
    "who made you": "I was built by an human.",
    "help": "You can ask my name, tell me a joke request, ask what I can do, or type 'bye' to exit.",
    "thank you": "You're welcome!",
    "thanks": "No problem at all!",
    "how old are you": "I was just born this week — freshly compiled!",
}

# Layer 2: Keyword Matching


keyword_responses = {
    "joke": "Why do programmers prefer dark mode? Because light attracts bugs!",
    "name": f"I go by {BOT_NAME}.",
    "what can you do": "I can chat using pre-defined rules — ask me about myself, or say hello!",
    "capabilities": "Right now I only understand rule-based responses, no deep learning yet.",
    "weather": "I can't check live weather yet — that needs an API, coming in a future project!",
    "sad": "Sorry to hear that. I hope your day gets better soon.",
    "happy": "That's great to hear! Glad you're doing well.",
    "love": "Aww, that's sweet of you to say.",
    "who are you": f"I'm {BOT_NAME}, DecodeLabs' Project 1 chatbot.",
}

exit_commands = ["bye", "exit", "quit"]

DEFAULT_REPLY = "I do not understand that yet. Try 'help' to see what I can do."


def get_response(user_input: str) -> str:
    """Two-layer lookup:
    1. Exact match against `responses` (fastest, most precise).
    2. Keyword match against `keyword_responses` (catches natural phrasing).
    3. Falls back to a default message if nothing matches.
    """
    # Layer 1: exact match
    if user_input in responses:
        return responses[user_input]

    # Layer 2: keyword match (does any known keyword appear in the input?)
    for keyword, reply in keyword_responses.items():
        if keyword in user_input:
            return reply

    # Layer 3: fallback
    return DEFAULT_REPLY


def main():
    print(f"{BOT_NAME}: Hello! I'm your rule-based assistant. Type 'bye' to exit.")

    while True:  # Phase: The Heartbeat - continuous loop
        raw_input_text = input("You: ")

        # Phase 1: Input Sanitization
        clean_input = raw_input_text.lower().strip()

        # Exit Strategy
        if clean_input in exit_commands:
            print(f"{BOT_NAME}: Goodbye! Have a great day.")
            break

        # Process + Respond
        reply = get_response(clean_input)
        print(f"{BOT_NAME}:", reply)


if __name__ == "__main__":
    main()
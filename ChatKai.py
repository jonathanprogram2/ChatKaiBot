# Rule-Based Chatbot System
# This simple chat uses predefined rules (if-elif-else) to respond to user input

def chatbot():
    print("🤖 ChatKai: Hello! I'm ChatKai. Ask me anything you want or type 'bye' to exit. \n")

    while True:
        user_input = input("You: ").lower().strip()  # Get user input and normalize it

        # Rule 1: Greetings
        if any(word in user_input for word in ["hello", "hi", "hey"]):
            print("🤖 ChatKai: Hi there! How can I assist you today?")

        # Rule 2: Farewell
        elif any(word in user_input for word in ["bye", "goodbye", "see you"]):
            print("🤖 ChatKai: Goodbye! Have a great day!")
            break # Exit the Loop

        # Rule 3: Asking for the time
        elif "time" in user_input:
            print("🤖 ChatKai: Haha, Sorry buddy, I'm not a clock – but your device should have the time ready and waiting for you!") 
        
        # Rule 4: Asking about the chatbot itself
        elif "who are you" in user_input or "what are you" in user_input:
            print("🤖 ChatKai: I'm ChatKai, a simple rule-based chatbot created with Python.")

        # Rule 5: Asking for help or features
        elif "help" in user_input or "what can you do" in user_input:
            print("🤖 ChatKai: I can greet you, answer simple questions, and keep you company!")

        #Rule 6: Asking for a fun fact
        elif "fun fact" in user_input:
            print("🤖 ChatKai: Did you know that honey never spoils? Archaeologists found 3,000-year-old honey in Egyptian tombs!")

        # Rule 7: Weather (example response)
        elif "weather" in user_input:
            print("🤖 ChatKai: I'm not plugged into real-time weather data, but here's hoping it's the kind of day that makes you want to high-five a stranger!")
        
        # Rule 8: Jokes
        elif "joke" in user_input:
            print("🤖 ChatKai: Why did the computer catch a cold? Because it left its Windows open!")

        # Default Rule: Unknown input
        else:
            print("🤖 ChatKai: I'm not sure how to respond to that. Try asking me something else.")
        

chatbot();  # Run the chatbot

    
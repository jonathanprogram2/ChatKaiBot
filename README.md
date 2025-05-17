# 🤖 Rule-Based Chatbot: ChatKai

A simple Python chatbot built using rule-based logic (no machine learning). This project demonstrates how early AI systems functioned using predefined rules and keyword detection.

---

## 📌 3 Project Ideas

### 1. Rule-Based Chatbot
- **What it does:** This system simulates a conversation with a user, like a basic virtual assistant or customer support agent.  
- **How it works using rules:** It uses predefined rules and keyword matching to detect common inputs (like greetings or questions) and responds with preset messages. For example, if the user says "hello", the bot replies "Hi! How can I help you?"

---

### 2. Movie Recommendation System (Rule-Based)
- **What it does:** This system recommends movies to users based on their preferred genre, mood, or language.  
- **How it works using rules:** It follows if-then logic to suggest a movie. For instance, if the user selects "sci-fi" and "adventure", the system recommends a list of sci-fi adventure films.

---

### 3. Rule-Based Recipe Recommendation System
- **What it does:** This system suggests recipes to users based on the ingredients they have available at home.  
- **How it works using rules:** It uses predefined ingredient combinations to match user inputs. If a user enters "eggs, milk, and flour", it might recommend pancakes using a rule that checks for those ingredients.

---

## ⭐ Project I Chose: Rule-Based Chatbot

I chose the rule-based chatbot because it gives me a chance to explore natural language interaction in a simple, structured way. I find it interesting how a chatbot can simulate conversation using just rules and logic, and I’d like to build one that responds like a basic customer service bot.

---

## 🧠 Rule-Based Chatbot: Logic and Rules Outline

### General Idea
The chatbot will:
- Respond to user inputs based on detected keywords or phrases.
- Use simple `if-elif-else` logic to match known patterns.
- Return predefined responses based on those patterns.

---

### 🔁 Rule Categories

1. **Greetings**  
   IF user input contains “hello” / “hi” / “hey”  
   THEN reply: `"Hi there! How can I help you today?"`

2. **Farewells**  
   IF user input contains “bye” / “goodbye” / “see you”  
   THEN reply: `"Goodbye! Have a great day!"`

3. **Asking about Time**  
   IF user input contains “time”  
   THEN reply: `"I'm not a clock, but you can check the time on your device!"`

4. **Asking about the Bot**  
   IF user input contains “who are you” / “what are you”  
   THEN reply: `"I'm a simple rule-based chatbot built to assist you!"`

5. **Asking for Help**  
   IF user input contains “help” / “what can you do”  
   THEN reply: `"I can answer basic questions, say hello, and give simple info!"`

6. **Unknown or Unrecognized Input**  
   ELSE reply: `"Sorry, I didn't understand that. Can you rephrase?"`

---

### 💬 Sample Input & Output

You: hi  
🤖 ChatKai: Hi there! How can I assist you today?

You: time  
🤖 ChatKai: Haha, Sorry buddy, I'm not a clock – but your device should have the time ready and waiting for you!

You: who are you  
🤖 ChatKai: I'm ChatKai, a simple rule-based chatbot created with Python.

You: who  
🤖 ChatKai: I'm not sure how to respond to that. Try asking me something else.

---

## 📝 Reflection

### Project Overview:
This project involved designing a practical, rule-based chatbot called **ChatKai** that responds to user inputs based on predefined logic. The system uses conditional `if-elif-else` statements to detect keywords in the user's input (such as greetings or questions) and return appropriate responses. The goal was to simulate an early form of artificial intelligence using straightforward rule-based decision-making.

---

### Challenges:

**Defining Effective Keyword Rules:**  
One of the key challenges was determining which words or phrases the chatbot should recognize and how flexible those rules should be. Since the system doesn’t learn from experience, each response had to be carefully mapped to expected input patterns.

**Handling Unexpected or Ambiguous Input:**  
Users may input incomplete or vague questions (e.g., just “who”), which don't exactly match any rule. To address this, I added a default fallback response to guide users toward more recognizable input.

**Making Responses Feel Natural:**  
Although the chatbot is rule-based, I wanted it to feel friendly and conversational. This required thoughtful phrasing of replies while keeping the code simple and readable.



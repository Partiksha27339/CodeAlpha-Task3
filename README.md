# CodeAlpha-Task3
CodeAlpha Internship Tasks 3 
Here's a summary of your chatbot_game code, explained in points:
Code Summary (in Points):
1. Function Definition:
chatbot_game(user_input) handles user input and provides predefined responses.
2. Input Conversion:
The input is converted to lowercase using text = user_input.lower() for easier comparison.
3. Keyword Matching (if-elif chain):
The function checks for keywords:
If user says "hello" or "hi" → responds with "HELLO!"
If user says "how are you" → responds with "I'm fine."
If user says "bye" or "goodbye" → responds with "Goodbye! It is nice talking with you."
If user says "thanks" or "thank you" → responds with "You're welcome!"
Otherwise → "Sorry, I don't understand. Can you please repeat it again"
4. Initial Greeting:
The chatbot starts by printing:
"Chatbot: Hello! Type 'bye' to exit."
5. Infinite Loop:
The program repeatedly asks for user input.
If the input is "bye" or "goodbye", it responds, then breaks the loop to end the conversation.
Otherwise, it keeps responding using the chatbot_game function.

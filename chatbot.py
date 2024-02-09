def simple_chatbot():
    print("Simple Chatbot: Hello! How can I help you today?")
    
    while True:
        user_input = input("You: ").lower()

        # Define the chatbot responses
        responses = {
            'hello': 'Hello!',
            'how are you?': 'I am a just an python programmer Akshay Mistry, but I am doing well. How about you?',
            'fine': 'Cool',
            'bye': 'Goodbye! Have a great day!',
            'thank you': 'You\'re welcome!',
            'default': 'I\'m not sure how to respond to that. Can you please rephrase or ask something else?'
        }

        # Check if the user input is in the responses dictionary
        response = responses.get(user_input, responses['default'])

        # Print the chatbot's response
        print("Chatbot:", response)

        # Check if the user wants to end the conversation
        if user_input == 'bye':
            break

if __name__ == "__main__":
    simple_chatbot()

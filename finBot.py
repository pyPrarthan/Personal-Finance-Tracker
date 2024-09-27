from email import message
import time
import openai
import os

# Setting up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def talk_with_chatbot():
    print("You can ask the chatbot for financial advice. Type 'exit' to go back to the main menu.")

    while True:
        user_input = input('\nYou: ')
        if user_input.lower() == 'exit':
            break
        
        # Sending the user response to the GPT model 
        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",  # Use the appropriate model name
                messages=[
                    {"role": "system", "content": "You are FinBot, a finance expert."},
                    {"role": "user", "content": user_input}
                ],
                max_tokens=150,  # Set the maximum number of tokens for the response
                temperature=0.7  # Adjust creativity level (0 = deterministic, 1 = very creative)
            )
            
            # Extracting and printing the response from the API
            if response.choices:
                message_content = response.choices[0].message.content
                if message_content is not None:
                    reply = message_content.strip()
                    print(f"Chatbot: {reply}")
                else:
                    print("The chatbot didn't return any content.")
            else:
                print("No response from the chatbot.")
        
        except Exception as e:
            print(f"Error occured: {e}")

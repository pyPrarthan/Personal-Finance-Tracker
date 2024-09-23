from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

class FinanceChatBot:
    def __init__(self):
        # Create a chatbot instance
        self.chatbot = ChatBot('FinanceBot')

        # Trainer for the chatbot
        self.trainer = ListTrainer(self.chatbot)
        
        # Training the chatbot with basic financial advice
        self.train_bot()

    def train_bot(self):
        conversation = [
            "How can I save more money?",
            "You can start by setting aside a fixed amount every month and cutting unnecessary expenses.",
            "What's the best way to invest?",
            "A good strategy is to diversify your investments across stocks, bonds, and savings accounts.",
            "How do I create a budget?",
            "List all your income and expenses, then allocate a specific amount to each category to avoid overspending.",
            "How can I reduce debt?",
            "Start by paying off high-interest debt first and avoid taking on new debt."
        ]
        
        self.trainer.train(conversation)
        
    def get_response(self, user_input):
        return self.chatbot.get_response(user_input)

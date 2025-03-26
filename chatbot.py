import random

class BankingChatbot:
    def __init__(self):
        self.responses = {
            "greeting": ["Hello! How can I assist you today?", "Hi there! How can I help you with your banking needs?"],
            "balance": ["Your current balance is $1,234.56.", "You have $2,345.67 in your account."],
            "transfer": ["How much would you like to transfer?", "Please provide the amount and the recipient's account number."],
            "goodbye": ["Thank you for using our services. Have a great day!", "Goodbye! Feel free to reach out if you need any more assistance."],
            "help": ["You can ask me about your account balance, transfer funds, or any other banking-related queries."]
        }
        self.balance = 1234.56  # Example balance

    def get_response(self, user_input):
        user_input = user_input.lower()
        if "hello" in user_input or "hi" in user_input:
            return random.choice(self.responses["greeting"])
        elif "balance" in user_input:
            return f"Your current balance is ${self.balance:.2f}."
        elif "transfer" in user_input:
            return random.choice(self.responses["transfer"])
        elif "bye" in user_input or "goodbye" in user_input:
            return random.choice(self.responses["goodbye"])
        elif "help" in user_input:
            return random.choice(self.responses["help"])
        else:
            return "I'm sorry, I didn't understand that. Can you please rephrase?"

    def transfer_funds(self, amount, recipient_account):
        if amount > self.balance:
            return "Insufficient funds for this transfer."
        else:
            self.balance -= amount
            return f"Successfully transferred ${amount:.2f} to account {recipient_account}. Your new balance is ${self.balance:.2f}."

if __name__ == "__main__":
    bot = BankingChatbot()
    print("Banking Chatbot: Hello! How can I assist you today?")
    while True:
        if "bye" in user_input.lower() or "goodbye" in user_input.lower():
            print(f"Banking Chatbot: {bot.get_response(user_input)}")
            break
        elif "transfer" in user_input.lower():
            amount = float(input("Banking Chatbot: Please enter the amount to transfer: "))
            recipient_account = input("Banking Chatbot: Please enter the recipient's account number: ")
            print(f"Banking Chatbot: {bot.transfer_funds(amount, recipient_account)}")
        else:
            print(f"Banking Chatbot: {bot.get_response(user_input)}")
import random

def greet():
    greetings = ["Hello! Welcome to our customer support.", "Hi there! How can I assist you today?", "Hey! How may I help you?"]
    return random.choice(greetings)

def respond_to_inquiry(inquiry):
    if "order" in inquiry:
        return "For inquiries related to orders, please contact our support team at support@example.com."
    elif "refund" in inquiry or "return" in inquiry:
        return "If you need assistance with refunds or returns, please visit our returns policy page on our website."
    elif "account" in inquiry or "login" in inquiry:
        return "For account-related issues or login assistance, please try resetting your password or contact support."
    else:
        return "I'm sorry, I'm not sure how to assist with that. You can try asking a different question or contact support for help."

def main():
    print("Bot:", greet())
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: Thank you for using our customer support chat. Have a great day!")
            break
        response = respond_to_inquiry(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()
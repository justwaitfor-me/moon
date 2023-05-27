from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Erstelle einen ChatBot
chatbot = ChatBot('Mein Chatbot')

# Erstelle einen Trainer und trainiere den ChatBot
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english.greetings')

# Interaktion mit dem Chatbot
while True:
    user_input = input('Du: ')
    response = chatbot.get_response(user_input)
    print('Chatbot:', response)

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer               #importing libarries
import os                                                #importing Operating system

bot=ChatBot('SUHANA')                                  #Defining the name and trainer for Chatbot
bot.set_trainer(ListTrainer)

for files in os.listdir('C:/chatterbot-corpus-master/chatterbot_corpus/data/english/'):                    #accessing the files
        data=open('C:/chatterbot-corpus-master/chatterbot_corpus/data/english/'+files,'r').readlines()     #Replace all '\' with '/' to avoid end of line and end the path with '/'
        bot.train(data)

while True:
    message=input('You:')
    if message.strip!='Bye' or message.strip!='bye':
        reply=bot.get_response(message)
        print('ChatBot:',reply)
    else:
        print("ChatBot:It was nice Talking to you")
        break
        
        

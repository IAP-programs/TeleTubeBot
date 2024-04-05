import telebot
import main
import time
import os
from telegram import Bot
os.system("clear")
def file(name, data) :
 file = open(name, "a")
 try :
  file.write(data) 
 except :
  print("error to write the file")
# Replace 'YOUR_TOKEN' with your actual bot token obtained from BotFather
with open("bot_token", "r") as f1 :
   token = f1.read()
   token = token.replace("\n", "")
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['/help'])
def send_welcome(message):
    bot.reply_to(message, "/start to start the telegram bot")
"""
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    bot.reply_to(message, ""🚨 Subscription Required 🚨

To access the bot's features, please subscribe to my YouTube channel first. Your subscription helps support my work and allows me to continue improving the bot for you.

Here's the link to subscribe : https://m.youtube.com/channel/UCGZd96UgAuHdsW-PS-45SSw"")
    bot.send_message(message.chat.id, "wait i want check it ")
    m = main.check_new_subscribers()
    m = str(m)
    if  m == "New subscriber detected!" :
     bot.send_message(message.chat.id,""🎉 Thank You for Subscribing! 🎉

Your support means a lot! You can now access all the bot's features. Happy exploring! 🚀
""
     file = open("user_id", "a")
     file.write(user_id+"\n")
     file.close()
"""#####





@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    user_id = str(user_id)
    print("user started user_id : "+user_id)
    file = open("user_id", "r")
    file = file.read()
    file = str(file)
    
    if user_id in file :
        print(user_id+" this user subscriped ")
    else :
        bot.reply_to(message, """🚨 Subscription Required 🚨

To access the bot's features, please subscribe to my YouTube channel first. Your subscription helps support my work and allows me to continue improving the bot for you.

Here's the link to subscribe : https://m.youtube.com/channel/UCGZd96UgAuHdsW-PS-45SSw""")
        m = main.check_new_subscribers()
        m = str(m)
        if  m == "New subscriber detected!" :
            bot.send_message(message.chat.id,"""🎉 Thank You for Subscribing! 🎉

Your support means a lot! You can now access all the bot's features. Happy exploring! 🚀
""")
            #
            file = open("user_id", "a")
            file.write(user_id+"\n")
            file.close()


#@bot.message_handler(func=lambda message: message.text.lower() == 'hi')
#def reply_hello(message):
    #bot.reply_to(message, "Hello!")

#@bot.message_handler(func=lambda message: message.text.lower() == 'hello')
#def reply_hello(message):



@bot.message_handler(func=lambda message: True)
def echo_all(message):
    user_id = message.from_user.id
    chat_id = user_id
    user_id = str(user_id)
    print("message from "+user_id+" message "+message.text)
    file = open("messages.txt", "a")
    file.write("\n"+"message from "+user_id+" message "+message.text)
    file.close()
    file = open("user_id", "r")
    file = file.read()
    file = str(file)
    if user_id in file :
        message1 = main.reply(message.text)
        data_type = message1[1]
        message1 = message1[0]
        if data_type == "string" :
           message1 = message1.replace("string ", "")
           bot.reply_to(message, message1)
        elif data_type == "file" :
           message1 = message1.replace("file ", "")
           file_path = message1
           with open(file_path, 'rb') as file:
               bot.send_document(chat_id, file)
        #
    else :
       bot.reply_to(message, """🚨 Subscription Required 🚨

To access the bot's features, please subscribe to my YouTube channel first. Your subscription helps support my work and allows me to continue improving the bot for you.

Here's the link to subscribe : https://m.youtube.com/channel/UCGZd96UgAuHdsW-PS-45SSw""")
       m = main.check_new_subscribers()
       if  m == "New subscriber detected!" :
           bot.send_message(message.chat.id,"""🎉 Thank You for Subscribing! 🎉

Your support means a lot! You can now access all the bot's features. Happy exploring! 🚀
""")
           file = open("user_id", "a")
           file.write(user_id+"\n")
           file.close()

"""
@bot.message_handler(content_types=['text'])
def check_message(message):
    # Check if the message contains the word "fuck"
    if "fuck" in message.text.lower():
        # Check if the message is from a group
        if message.chat.type == "group" or message.chat.type == "supergroup":
            # Remove the member who sent the message
            bot.kick_chat_member(message.chat.id, message.from_user.id)
            file("memberse_remove_list", f"remove user_id : {message.from_user.id}, chat_id : {message.chat.id}")
            print(f"remove user_id : {message.from_user.id}, chat_id : {message.chat.id}")
            bot.reply_to(message, "This group does not tolerate inappropriate language. You have been removed.")
        else:
            bot.reply_to(message, "This command can only be used in groups.")

"""
bot.polling()

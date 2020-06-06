import config
import telebot
import re
import sqlite3
import datetime
from telebot import types
bot = telebot.TeleBot(config.token)
@bot.message_handler(commands=['start', 'help'])
def    send_welcome(message):
    with open('data.txt', 'a') as inFile:
        line = "User logs : \n"
        line1 = "    User name: \n"+str(message.from_user.first_name)


        line2  = "\n     Time: \n"+str(datetime.datetime.today())

        line3 = "\n    Messages text : \n" + str(message.text)
        line4 = "\n    date : " + str(message)+"\n"
        print(line)
        print(line)
        print(line)
        print(line)
        inFile.write (line)
        inFile.write (line1)
        inFile.write (line2)
        inFile.write (line3)
        inFile.write (line4)
        inFile.close()

    dat1= str(message.from_user.first_name)
    dat2 = str(datetime.datetime.today())
    dat3= str(message.text)
    db_1 = sqlite3.connect("log.db")
    sql_1 = db_1.cursor()
    sql_1.execute("CREATE TABLE IF NOT EXISTS users(nickname TEXT,time TEXT,mesage_text TEXT)")
    db_1.commit()




    sql_1.execute(f"INSERT INTO users VALUES(?,?,?)",(dat1,dat2,dat3))
    db_1.commit()

    print(message)
    print(str(message.text))
    print(message.from_user.first_name)

    bot.send_message(message.chat.id ,"Привет "+ str(message.from_user.first_name)+" 😎🖐 \nВот что я могу: Тут ты можешь найть номера и то откуда они к примеру напиши боту Soroca или Botanicca  и ты наидёшь номера йз базы даных связыных с этими местами или просто напишь  679 чтобы наить такие номера.База даных скоро обновитца!")
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):

    with open('data.txt', 'a') as inFile:
        line = "User logs : \n"
        line1 = "    User name: \n"+str(message.from_user.first_name)


        line2  = "\n     Time: \n"+str(datetime.datetime.today())

        line3 = "\n    Messages text : \n" + str(message.text)
        line4 = "\n    date : " + str(message)+"\n"
        print(line)
        print(line)
        print(line)
        print(line)
        inFile.write (line)
        inFile.write (line1)
        inFile.write (line2)
        inFile.write (line3)
        inFile.write (line4)
        inFile.close()

    db = sqlite3.connect("date.db")
    sql = db.cursor()
    inputdate = message.text
    for value in sql.execute("SELECT nickname,number,region,pageid FROM  users"):
        if re.search(inputdate, str(value)):
             print(value)

             bot.send_message(message.chat.id, "Вот что было наидено:\n"+str(value))
             if value[3] != "NON ID":
                 bot.send_message(message.chat.id, "Сылка на обьявление:\n"+"https://999.md/ru/" + str(value[3]))

    dat1= str(message.from_user.first_name)
    dat2 = str(datetime.datetime.today())
    dat3= str(message.text)
    db_1 = sqlite3.connect("log.db")
    sql_1 = db_1.cursor()
    sql_1.execute("CREATE TABLE IF NOT EXISTS users(nickname TEXT,time TEXT,mesage_text TEXT)")
    db_1.commit()




    sql_1.execute(f"INSERT INTO users VALUES(?,?,?)",(dat1,dat2,dat3))
    db_1.commit()

if __name__ == '__main__':
     bot.polling(none_stop=True)
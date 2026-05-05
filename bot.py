import telebot
import random
TOKEN = '8667196115:AAE4JtvInpOgYsE9c0KO-fm7ONi-Oa1Rb8U'
bot = telebot.Telebot(TOKEN)
game_inventory = ['m', 'up', 'd', 'l', 'lup', 'ld', 'r', 'rup', 'rd']

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Играть будем в крестик нолик, и это не обсуждается")

@bot.message_handler(commands=['end'])
def end(message):
    bot.send_message(message.chat.id, "Не прихожи больше")

@bot.message_handler(content_types=['text'])
def echo(message):
    choice_player = message.text.lower()
    if choice_player in game_inventory:
        choice_bot = random.choice(game_inventory)
        if choice_player == 'm':
            if choice_bot == 'l':
                bot.send_message(message.chat.id, choice_bot)
                bot.send_message(message.chat.id, " | | \n"
                                                  "O|X| \n"
                                                  " | | \n")
                if choice_player == 'lup':
                    if choice_bot == 'ld':
                        bot.send_message(message.chat.id, choice_bot)
                        bot.send_message(message.chat.id, "X| | \n"
                                                          "O|X| \n"
                                                          "O| | \n")
                        if choice_player == 'r':
                            if choice_bot == 'd':
                                bot.send_message(message.chat.id, choice_bot)
                                bot.send_message(message.chat.id, "X| | \n"
                                                                  "O|X|X\n"
                                                                  "O|O| \n")
                                if choice_player == 'rup':
                                    if choice_bot == 'rd':
                                        bot.send_message(message.chat.id, choice_bot)
                                        bot.send_message(message.chat.id, "X| |X\n"
                                                                          "O|X|X\n"
                                                                          "O|O|O\n")
                                        bot.send_message(message.chat.id, "А я победил? Я ПОБЕДИЛ ХАХАХХАХАХАХ")
                                    elif choice_bot == 'up':
                                        bot.send_message(message.chat.id, choice_bot)
                                        bot.send_message(message.chat.id, "X|O|X\n"
                                                                          "O|X|X\n"
                                                                          "O|O| \n")
                                        if choice_player == 'rd':
                                            bot.send_message(message.chat.id, choice_bot)
                                            bot.send_message(message.chat.id, "X|O|X\n"
                                                                              "O|X|X\n"
                                                                              "O|O|X\n")
                                            bot.send_message(message.chat.id, "Вы победили мистер свин... вонючка")
                            elif choice_bot == 'up':
                                bot.send_message(message.chat.id, choice_bot)
                                bot.send_message(message.chat.id, "X|O| \n"
                                                                  "O|X|X\n"
                                                                  "O| | \n")
                            elif choice_bot == 'rup':
                                bot.send_message(message.chat.id, choice_bot)
                                bot.send_message(message.chat.id, "X| |O\n"
                                                                  "O|X|X\n"
                                                                  "O| | \n")
                            elif choice_bot == 'rd':
                                bot.send_message(message.chat.id, choice_bot)
                                bot.send_message(message.chat.id, "X| |O\n"
                                                                  "O|X|X\n"
                                                                  "O| | \n")
                        elif choice_player == 'rd':
                            bot.send_message(message.chat.id, choice_bot)
                            bot.send_message(message.chat.id, "X| | \n"
                                                              "O|X| \n"
                                                              "O| |X\n")
                            bot.send_message(message.chat.id, "Я МИСКЛИКНУЛ ЧЕРТ")
                    elif choice_bot == 'd':
                        bot.send_message(message.chat.id, choice_bot)
                        bot.send_message(message.chat.id, "X| | \n"
                                                          "O|X| \n"
                                                          " |O| \n")
                    elif choice_bot == 'up':
                        bot.send_message(message.chat.id, choice_bot)
                        bot.send_message(message.chat.id, "X|O| \n"
                                                          "O|X| \n"
                                                          " | | \n")
                    elif choice_bot == 'rup':
                        bot.send_message(message.chat.id, choice_bot)
                        bot.send_message(message.chat.id, "X| |O\n"
                                                          "O|X| \n"
                                                          " | | \n")
                    elif choice_bot == 'r':
                        bot.send_message(message.chat.id, choice_bot)
                        bot.send_message(message.chat.id, "X| | \n"
                                                          "O|X|O\n"
                                                          " | | \n")
            elif choice_bot == 'lup':
                bot.send_message(message.chat.id, choice_bot)
                bot.send_message(message.chat.id, "O| | \n"
                                                  " |X| \n"
                                                  " | | \n")
            elif choice_bot == 'ld':
                bot.send_message(message.chat.id, choice_bot)
                bot.send_message(message.chat.id, " | | \n"
                                                  " |X| \n"
                                                  "O| | \n")
            elif choice_bot == 'up':
                bot.send_message(message.chat.id, choice_bot)
                bot.send_message(message.chat.id, " |O| \n"
                                                  " |X| \n"
                                                  " | | \n")
            elif choice_bot == 'd':
                bot.send_message(message.chat.id, choice_bot)
                bot.send_message(message.chat.id, " | | \n"
                                                  " |X| \n"
                                                  " |O| \n")
            elif choice_bot == 'rup':
                bot.send_message(message.chat.id, choice_bot)
                bot.send_message(message.chat.id, " | |O\n"
                                                  " |X| \n"
                                                  " | | \n")
            elif choice_bot == 'r':
                bot.send_message(message.chat.id, choice_bot)
                bot.send_message(message.chat.id, " | | \n"
                                                  " |X|O\n"
                                                  " | | \n")
            elif choice_bot == 'rd':
                bot.send_message(message.chat.id, choice_bot)
                bot.send_message(message.chat.id, " | | \n"
                                                  " |X| \n"
                                                  " | |O\n")

bot.polling()
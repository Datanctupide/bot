import telebot
import random
TOKEN = '8667196115:AAE4JtvInpOgYsE9c0KO-fm7ONi-Oa1Rb8U'
bot = telebot.TeleBot(TOKEN)
game_inventory = ['Да', 'Нарвное...', 'Возможно', 'Я скучаю по своей жене...', 'Нет', 'Я так не думаю', 'эээээээмм... хз', 'Кто здесь?', 'Не думаю']

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Скажи мне что то и отвечу")

@bot.message_handler(commands=['end'])
def end(message):
    bot.send_message(message.chat.id, "Не прихожи больше")

@bot.message_handler(content_types=['text'])
def echo(message):
    choice_player = input()
    choice_bot = random.choice(game_inventory)
    x = 0
    while x == 10:
            if choice_bot == 'Да':
                bot.send_message(message.chat.id, choice_bot)
                bot.send_message(message.chat.id, 'Да')
            elif choice_bot == 'Нарвное...':
                bot.send_message(message.chat.id, choice_bot)
                bot.send_message(message.chat.id, 'Нарвное...')
            elif choice_bot == 'Возможно':
                bot.send_message(message.chat.id, choice_bot)
                bot.send_message(message.chat.id, 'Возможно')
            elif choice_bot == 'Я скучаю по своей жене...':
                bot.send_message(message.chat.id, choice_bot)
                bot.send_message(message.chat.id, 'Я скучаю по своей жене...')
            elif choice_bot == 'Нет':
                bot.send_message(message.chat.id, choice_bot)
                bot.send_message(message.chat.id, 'Нет')
            elif choice_bot == 'Я так не думаю':
                bot.send_message(message.chat.id, choice_bot)
                bot.send_message(message.chat.id, 'Я так не думаю')
            elif choice_bot == 'эээээээмм... хз':
                bot.send_message(message.chat.id, choice_bot)
                bot.send_message(message.chat.id, 'эээээээмм... хз')
            elif choice_bot == 'Кто здесь?':
                bot.send_message(message.chat.id, choice_bot)
                bot.send_message(message.chat.id, 'Кто здесь?')
            elif choice_bot == 'Не думаю':
                bot.send_message(message.chat.id, choice_bot)
                bot.send_message(message.chat.id, 'Не думаю')
            x += 1

bot.polling()
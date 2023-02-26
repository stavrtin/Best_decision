#pip install pyTelegramBotAPI

from datetime import datetime
import telebot
from telebot import types
import config
import view
import model

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["start"])
def start(message): # ----
    view.start_menu(message)

@bot.message_handler(commands=["admin"])
def admin(message):  # ----
    view.admin_psw_menu(message)

@bot.message_handler(content_types=["text"])
def bot_messages(message): # --------------------формируем список ВПС для выбора и дальнейшего проваливания к ФИО ---
    print(f'произошло нажание кнопки или введен текст {message.text}')
    if message.chat.type == 'private':      # --- если это не телеграм канал, а личное сообщение --
        # ------------ работа начального меню ----------
        if message.text == '✉ Справка о работе бота':
            # bot.send_message(message.chat.id, 'Тут мы распишем, как же получить телефон и как его сдать')
            view.info_text(message)

        elif message.text == '✅ Получить телефон':
            text_status = 'где ВЫДАЁТСЯ ☏'
            view.menu_choise_vps(message, text_status)

        elif message.text == '🔒 Вернуть телефон':
            text_status = 'куда СДАЕТСЯ ☎'
            view.menu_choise_vps(message, text_status)

        elif message.text == '+Qwer':
            view.admin_menu(message)

        elif message.text == '↪️В меню':
            view.start_menu(message)

        else:
            # bot.send_message(message.chat.id, "Выберете действие, указанное на кнопках, или /start для перезапуска БОТа ")
            view.wrong_choise(message)




@bot.message_handler(content_types=["text"])
def choice_fio_from_vps(message, text_status):
    if message.text == '↪️В меню':
        view.start_menu(message)
    # ----- проверка Админского пароля -----
#
    else:
        view.menu_choise_fio(message, text_status)
# -------------

# @bot.message_handler(content_types=["text"])
#
# def check_admin_psw(message, text_status):
#     if message.text == 'Qwer':
#         view.admin_menu(message)
#
#     else:
#         view.admin_psw_menu(message)
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# The above encoding declaration is required and the file must be saved as UTF-8

'''Создаем меню для управления ботом'''

# https://yandex.ru/video/preview/14627769197229213338  # -- откуда видос. Расписано отлично
# http://text-image.ru/index/symbols/0-10   -- рисуночки отсюда----

#pip install pyTelegramBotAPI
from datetime import datetime
import telebot
from telebot import types
import config
import view
import model


# bot = telebot.TeleBot(config.token)  # Подключили токен

# vps_list = ['Бутово','Дегунино','Ростокино','Куркино','Царицыно']
#
# vps_dict = {'Бутово':['Гагарин', 'Леонов', 'Комаров'],
#             'Дегунино'  :['Дитов', 'Дерешкова', 'Драмаренко','Дкалов'],
#             'Ростокино' :['Титов-p', 'Терешкова-p', 'Крамаренко-p','Чкалов-p'],
#              'Куркино'   :['Титов-k', 'Терешкова-k', 'Крамаренко-k','Чкалов-k'],
#             'Царицыно'  :['Цитов', 'Церешкова', 'ЦКрамаренко','ЦЧкалов', 'ЦКожедуб', 'ЦПокрышкин'],
#              'Некрасовка':['Нитов', 'НТерешкова', 'НКрамаренко','НЧкалов'],
#              'Перово':['Питов', 'ПТерешкова', 'ПКрамаренко','ПЧкалов'],
#
#             }


# def dinamic_columns_button(markup, button_dict):
#     #  ----------------------------- функция формирования динамических рядов кнопок -----
#
#     item_back = types.KeyboardButton('↪️В меню')  # ---- создаем кнопку
#     menu_vps_dict = [types.KeyboardButton(i) for i in button_dict]  # --- сформировал список кнопок ---
#
#     # --------------------- разложить на две колонки кнопки ------
#     if len(menu_vps_dict) == 1:
#         markup.add(menu_vps_dict[0])
#         markup.add(item_back)   # -- если добавляем элементы отдельными порциями, то кнопки
#                                 # -- выводятся этими же порциями. Поэтому для ОТДЕЛЬНОГО отображения кнопки
#                                 # --- добавляем ее отдельно в меню  (делаем так для "НАЗАД" например)
#     elif len(menu_vps_dict) % 2 == 0:
#         for i in range(0, len(menu_vps_dict), 2):
#             markup.add(menu_vps_dict[i], menu_vps_dict[i + 1])
#         markup.add(item_back)
#     else:
#         i = 0
#         while i < len(menu_vps_dict):
#             if len(menu_vps_dict) - i >= 2:
#                 markup.add(menu_vps_dict[i], menu_vps_dict[i + 1])
#                 i += 2
#             else:
#                 markup.add(menu_vps_dict[i])
#                 i += 1
#         markup.add(item_back)
#     #  ----------------------------- функция формирования динамических рядов кнопок -----
#     return markup

#
# @bot.message_handler(commands=["start"])
# def start(message): # Название функции не играет никакой роли
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # -СОЗДАЮ меню markup (resize_keyb. что бы кнопки влезали)
#     item2 = types.KeyboardButton('✉ Справка о работе бота')  # ------ подменю1
#     item3 = types.KeyboardButton('✅ Получить телефон')  # ------подменю2
#     item4 = types.KeyboardButton('🔒 Вернуть телефон')  # -------подменю3
#
#     markup.add(item2, item3, item4)
#
#     # --- сразу меню не появится, надо пульнуть сообщения --
#     bot.send_message(message.chat.id, "Бот готов к регистрации записи в журнал приема/выдачи телефонов",
#                      reply_markup=markup)  # reply_markup - вывод меню
#
# # ---- создадим обработчик событий (по обработке ТЕКСТА, полученного из текста нажатого МЕНЮ)-----------
# @bot.message_handler(content_types=["text"])
# def bot_messages(message): # --------------------формируем список ВПС для выбора и дальнейшего проваливания к ФИО ---
#     print(f'произошло нажание кнопки или введен текст {message.text}')
#     if message.chat.type == 'private':      # --- если это не телеграм канал, а личное сообщение --
#         if message.text == '✉ Справка о работе бота':
#             bot.send_message(message.chat.id, 'Тут мы распишем, как же получить телефон и как его сдать')
#
#         elif message.text == '✅ Получить телефон':
#             # ---- ДИНАМИЧЕСКИ создать кнопки -------
#             markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)  # -СОЗДАЮ меню
#             dinamic_columns_button(markup, vps_dict)
#             # --- сразу меню не появится, надо пульнуть сообщения --
#             bot.send_message(message.chat.id, "Выберете ВПС, где ВЫДАЁТСЯ ☏\n или ↪️В меню",
#                              reply_markup=markup)  # reply_markup - вывод меню
#             bot.register_next_step_handler(message, choice_fio_from_vps_take_phone)  # --- переходим к выбору ВПС
#
#         elif message.text == '🔒 Вернуть телефон':
#             # ---- ДИНАМИЧЕСКИ создать кнопки -------
#             markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)  # -СОЗДАЮ меню
#             dinamic_columns_button(markup, vps_dict)
#             # --- сразу меню не появится, надо пульнуть сообщения --
#             bot.send_message(message.chat.id, "Выберете ВПС, куда СДАЕТСЯ ☎\n или ↪️В меню ", reply_markup=markup)
#             bot.register_next_step_handler(message, choice_fio_from_vps_return_phone)  # --- переходим к выбору ВПС
#
#             # bot.register_next_step_handler(message, add_message_into_db_return)
#         else:
#             bot.send_message(message.chat.id, "Выберете действие, указанное на кнопках внизу экрана... или /start для перезагрузки БОТа ")
#
#
# @bot.message_handler(content_types=["text"])
# def choice_fio_from_vps_take_phone(message):
#     if message.text == '↪️В меню':
#         start(message)
#
#     else:
#         vps_name = message.text # ------- получил имя ВПС (выбрано нажатием кнопки - текст КНОПКИ)
#         markup_choise_fio = types.ReplyKeyboardMarkup(resize_keyboard=True)  # -СОЗДАЮ меню markup
#         dinamic_columns_button(markup_choise_fio, vps_dict[vps_name])
#         # --- сразу меню не появится, надо пульнуть сообщения --
#         bot.send_message(message.chat.id, "Выберете кто ПОЛУЧАЕТ ☏\n или ↪️В меню ",
#                          reply_markup=markup_choise_fio)  # reply_markup - вывод меню
#         bot.register_next_step_handler(message, add_message_into_db_receive, vps_name)  # --- переходим к выбору FIO
#
# @bot.message_handler(content_types=["text"])
# def choice_fio_from_vps_return_phone(message):
#     if message.text == '↪️В меню':
#         start(message)
#
#     else:
#         vps_name = message.text # ------- получил имя ВПС (выбрано нажатием кнопки - текст КНОПКИ)
#         markup_choise_fio = types.ReplyKeyboardMarkup(resize_keyboard=True)  # -СОЗДАЮ меню markup
#         dinamic_columns_button(markup_choise_fio, vps_dict[vps_name])
#         # --- сразу меню не появится, надо пульнуть сообщения --
#         bot.send_message(message.chat.id, "Выберете кто СДАЁТ ☎\n или ↪️В меню ",
#                          reply_markup=markup_choise_fio)  # reply_markup - вывод меню
#         bot.register_next_step_handler(message, add_message_into_db_return, vps_name)  # --- переходим к выбору FIO


# def add_message_into_db_receive(message, vps_name):
#     if message.text == '↪️В меню':
#         start(message)
#
#     else:
#         fio = message.text
#         keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)  # Подключаем клавиатуру
#         button_phone = types.KeyboardButton(text='✅ Записать ВЫДАЧУ ☏ в журнал',
#                                             request_contact=True)  # Указываем название кнопки, которая появится у пользователя
#         item_back = types.KeyboardButton('Отмена\n↪️В меню')
#
#         keyboard.add(button_phone, item_back)  # Добавляем эту кнопку
#         bot.send_message(message.chat.id, f'Подготовлена запись ПОЛУЧЕНИЯ ☏ {fio} в журнал {vps_name}.\n',
#                                           # f'Для возврата в предыдущее меню введите "1" и нажмите ➤',
#                          reply_markup=keyboard)  # Дублируем сообщение
#         bot.register_next_step_handler(message, contact_receive, fio, vps_name)
#
# def add_message_into_db_return(message, vps_name):
#     if message.text == '↪️В меню':
#         start(message)
#     #тут функция записи в бд
#     else:
#         fio = message.text
#         keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)  # Подключаем клавиатуру
#         button_phone = types.KeyboardButton(text='✅ Записать ВОЗВРАТ ☎ в журнал',
#                                             request_contact=True)  # Указываем название кнопки, которая появится у пользователя
#         item_back = types.KeyboardButton('Отмена\n↪️В меню')
#
#         keyboard.add(button_phone, item_back)  # Добавляем эту кнопку
#         bot.send_message(message.chat.id, f'Подготовлена запись ВОЗВРАТА ☎ {fio} в журнал {vps_name}.\n',
#                          # f'Для возврата в предыдущее меню введите "1" и нажмите ➤',
#                          reply_markup=keyboard)  # Дублируем сообщение
#         bot.register_next_step_handler(message, contact_return, fio, vps_name)

#
# def contact_receive(message, fio, vps_name):
#     if message.text != None:
#         start(message)
#
#     else:
#         if message.contact is not None:  # Если присланный объект <strong>contact</strong> не равен нулю
#             phone_number = message.contact.phone_number
#             now = datetime.now()
#             date_ = now.strftime("%d-%m-%Y %H:%M")
#
#
#             doc = open('client.txt', 'a', encoding='utf-16')
#             # doc.write(f"\nВПС - {vps_name} - ФИО - {fio} Телефон - {phone_number} Получен - {date_}" )
#             doc.write(f"\n{vps_name};{fio};{phone_number};Получен;{date_}" )
#             doc.close()
#
#             bot.send_message(message.chat.id, f'{fio} получил {phone_number} в {vps_name} - {date_}') # -- вывод сообщ на экран телеф
#             start(message)
#
#
# def contact_return(message, fio, vps_name):
#     if message.text != None:
#         start(message)
#
#     else:
#         if message.contact is not None:  # Если присланный объект <strong>contact</strong> не равен нулю
#             phone_number = message.contact.phone_number
#             now = datetime.now()
#             date_ = now.strftime("%d-%m-%Y %H:%M")
#
#             doc = open('client.txt', 'a', encoding='utf-16')
#             # doc.write(f"\nВПС - {vps_name} - ФИО - {fio} Телефон - {phone_number} Сдан    - {date_}" )
#             doc.write(f"\n{vps_name}; {fio}; {phone_number}; Сдан; {date_}" )
#             doc.close()
#
#             bot.send_message(message.chat.id, f'{fio} СДАЛ {phone_number} в {vps_name} - {date_}') # -- вывод сообщ на экран телеф
#             start(message)



if __name__ == '__main__':
     bot.infinity_polling(none_stop=True)


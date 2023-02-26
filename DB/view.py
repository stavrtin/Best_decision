from telebot import types
import model
import controller


def admin_psw_menu(message):
    # ---- меню для ввода пароля Админа ---
    markup_admin = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('/start')  # ------ подменю1
    markup_admin.add(item1)
    controller.bot.send_message(message.chat.id, "Введите пароль Админа для внесения правок в БД",
                                reply_markup=markup_admin)

def admin_menu(message):
    # ----- создаю стартовое меню -------------
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # -СОЗДАЮ меню markup (resize_keyb. что бы кнопки влезали)
    item2 = types.KeyboardButton('👽 Добавить')  # ------ подменю1
    item3 = types.KeyboardButton('✎ Внести правки')  # ------подменю2
    item4 = types.KeyboardButton('✂ Удалить сведения')  # -------подменю3

    markup.add(item2, item3, item4)
    # --- сразу меню не появится, надо пульнуть сообщения --
    controller. bot.send_message(message.chat.id, "Открыт доступ для внесения правок в БД",
                     reply_markup=markup)  # reply_markup - вывод меню

def start_menu(message):
    # ----- создаю стартовое меню -------------
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # -СОЗДАЮ меню markup (resize_keyb. что бы кнопки влезали)
    item2 = types.KeyboardButton('✉ Справка о работе бота')  # ------ подменю1
    item3 = types.KeyboardButton('✅ Получить телефон')  # ------подменю2
    item4 = types.KeyboardButton('🔒 Вернуть телефон')  # -------подменю3

    markup.add(item2, item3, item4)
    # --- сразу меню не появится, надо пульнуть сообщения --
    controller. bot.send_message(message.chat.id, "Бот готов к регистрации записи в журнал приема/выдачи телефонов",
                     reply_markup=markup)  # reply_markup - вывод меню

def dinamic_columns_button(markup, button_dict):
    #  ----------------------------- функция формирования динамических рядов кнопок -----

    item_back = types.KeyboardButton('↪️В меню')  # ---- создаем кнопку
    menu_vps_dict = [types.KeyboardButton(i) for i in button_dict]  # --- сформировал список кнопок ---

    # --------------------- разложить на две колонки кнопки ------
    if len(menu_vps_dict) == 1:
        markup.add(menu_vps_dict[0])
        markup.add(item_back)   # -- если добавляем элементы отдельными порциями, то кнопки
                                # -- выводятся этими же порциями. Поэтому для ОТДЕЛЬНОГО отображения кнопки
                                # --- добавляем ее отдельно в меню  (делаем так для "НАЗАД" например)
    elif len(menu_vps_dict) % 2 == 0:
        for i in range(0, len(menu_vps_dict), 2):
            markup.add(menu_vps_dict[i], menu_vps_dict[i + 1])
        markup.add(item_back)
    else:
        i = 0
        while i < len(menu_vps_dict):
            if len(menu_vps_dict) - i >= 2:
                markup.add(menu_vps_dict[i], menu_vps_dict[i + 1])
                i += 2
            else:
                markup.add(menu_vps_dict[i])
                i += 1
        markup.add(item_back)
    #  ----------------------------- функция формирования динамических рядов кнопок -----
    return markup

def menu_choise_vps(message, text_status):

    # ---- ДИНАМИЧЕСКИ создать кнопки ВПС -------
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)  # -СОЗДАЮ меню
    dinamic_columns_button(markup, model.vps_dict)

    if text_status == 'где ВЫДАЁТСЯ ☏':
        controller.bot.send_message(message.chat.id, f"Выберете ВПС, *{text_status}*\n или ↪️В меню",
                                    reply_markup=markup, parse_mode= "Markdown")
    elif text_status == 'куда СДАЕТСЯ ☎':
        controller.bot.send_message(message.chat.id, f"Выберете ВПС, *{text_status}*\n или ↪️В меню",
                                    reply_markup=markup, parse_mode="Markdown")
    controller.bot.register_next_step_handler(message, controller.choice_fio_from_vps, text_status)  # --- переходим к выбору ВПС

def menu_choise_fio(message, status):
    # ----формируем список фамилий на основе выбора ВПС---

    vps_name = message.text  # ------- получил имя ВПС (выбрано нажатием кнопки - текст КНОПКИ)
    markup_choise_fio = types.ReplyKeyboardMarkup(resize_keyboard=True)  # -СОЗДАЮ меню markup

    # ----- если вдруг vps_name не из списка ВПС, прописанного в базе ----
    try:
        dinamic_columns_button(markup_choise_fio, model.vps_dict[vps_name])
        # --- сразу меню не появится, надо пульнуть сообщения --
        if status == 'где ВЫДАЁТСЯ ☏':
            controller.bot.send_message(message.chat.id, f"Выберете кто *ПОЛУЧАЕТ* ☏\n или ↪️В меню ",
                                        reply_markup=markup_choise_fio, parse_mode= "Markdown")  # reply_markup - вывод меню
        elif status == 'куда СДАЕТСЯ ☎':
            controller.bot.send_message(message.chat.id, f"Выберете кто *СДАЕТ* ☎\n или ↪️В меню ",
                                        reply_markup=markup_choise_fio, parse_mode= "Markdown")  # reply_markup - вывод меню

        controller.bot.register_next_step_handler(message, menu_confirm_records, vps_name, status)  # --- переходим к выбору FIO
    except:
        controller.bot.send_message(message.chat.id, "☹ Неверно указана ВПС...")
        start_menu(message)

def menu_confirm_records(message, vps_name, status):
    if message.text == '↪️В меню':
        start_menu(message)

    else:
        fio = message.text
        # ---------------- проверять фио на принадлежность к бд ------!!!!!!!!-------
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)  # Подключаем клавиатуру
        item_back = types.KeyboardButton('Отмена\n↪️В меню')

        if status == 'где ВЫДАЁТСЯ ☏':
            button_phone = types.KeyboardButton(text='✅ Записать ВЫДАЧУ ☏ в журнал',  request_contact=True)
            keyboard.add(button_phone, item_back)  # Добавляем эту кнопку
            controller.bot.send_message(message.chat.id, f'Подготовлена запись ПОЛУЧЕНИЯ ☏ *{fio}* в журнал {vps_name}.\n',
                                                        reply_markup=keyboard, parse_mode= "Markdown")  # Дублируем сообщение
        elif status == 'куда СДАЕТСЯ ☎':
            button_phone = types.KeyboardButton(text='⤵ Записать ВОЗВРАТ ☎ в журнал', request_contact=True)
            keyboard.add(button_phone, item_back)  # Добавляем эту кнопку
            controller.bot.send_message(message.chat.id, f'Подготовлена запись ВОЗВРАТА ☎ *{fio}* в журнал {vps_name}.\n',
                                                        reply_markup=keyboard, parse_mode= "Markdown")  # Дублируем сообщение
        controller.bot.register_next_step_handler(message, model.record_contact, fio, vps_name, status)

def confirm_recording_by_chat(message, fio, stat_tex, phone_number, vps_name, date_):
    controller.bot.send_message(message.chat.id, f'<b>{fio}</b> {stat_tex} {phone_number} в ВПС <b>{vps_name}</b> {date_}'
                                , parse_mode= "HTML")  # -- вывод сообщ на экран телеф

def wrong_choise(message):
    controller.bot.send_message(message.chat.id, "Выберете действие, указанное на кнопках, или /start для перезапуска БОТа ")

def info_text(message):
    controller.bot.send_message(message.chat.id, 'Тут мы распишем, как же получить телефон и как его сдать')
from datetime import datetime
import view
import controller
import psycopg2


# vps_list = ['Бутово','Дегунино','Ростокино','Куркино','Царицыно']
#
# vps_dict = {'Бутово':['Гагарин', 'Леонов', 'Комаров'],
#             'Дегунино'  :['Дитов', 'Дерешкова', 'Драмаренко','Дкалов'],
#             'Ростокино' :['Титов-p', 'Терешкова-p', 'Крамаренко-p','Чкалов-p'],
#              'Куркино'   :['Титов-k', 'Терешкова-k', 'Крамаренко-k','Чкалов-k'],
#             'Царицыно'  :['Цитов', 'Церешкова', 'ЦКрамаренко','ЦЧкалов', 'ЦКожедуб', 'ЦПокрышкин'],
#              'Некрасовка':['Нитов', 'НТерешкова', 'НКрамаренко','НЧкалов'],
#              'Перово':['Питов', 'ПТерешкова', 'ПКрамаренко','ПЧкалов'],
#             }



def read_db():
    # ----------- считываем БД со списком сотруднико, табл "spisok" -------
    my_db = psycopg2.connect(
        database="vps_jur",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )

    mycursor = my_db.cursor()

    vps_dict = {}

    # ---- готовый запрос на создание таблицы -----
    sql_all_rec = f"SELECT DISTINCT VPS_name FROM spisok"
    mycursor.execute(sql_all_rec)
    result = mycursor.fetchall()
    vps_uniq_list = [i[0] for i in result]

    # print(vps_uniq_list)

    for i in vps_uniq_list:
        sql_fio_from_vps = f"SELECT fio FROM spisok " \
                           f"where VPS_name = '{i}'"
        mycursor.execute(sql_fio_from_vps)
        result_fio = mycursor.fetchall()
        fio_list = [j[0] for j in result_fio]
        # print(fio_list)
        vps_dict.update({i: fio_list})

    # print(vps_dict)

    return vps_dict


def record_contact(message, fio, vps_name, status):
    if message.text != None:
        view.start_menu(message)

    else:
        if message.contact is not None:  # Если присланный объект <strong>contact</strong> не равен нулю
            phone_number = message.contact.phone_number
            now = datetime.now()
            date_ = now.strftime("%d-%m-%Y %H:%M")

            doc = open('client.txt', 'a', encoding='utf-16')
            # doc.write(f"\nВПС - {vps_name} - ФИО - {fio} Телефон - {phone_number} Получен - {date_}" )
            if status == 'где ВЫДАЁТСЯ ☏':
                stat_tex = 'ПОЛУЧИЛ'
                doc.write(f"\n{vps_name};{fio};{phone_number};Получен;{date_}" )

            elif status == 'куда СДАЕТСЯ ☎':
                stat_tex = 'СДАЛ'
                doc.write(f"\n{vps_name}; {fio}; {phone_number}; Сдан; {date_}")

            doc.close()
            view.confirm_recording_by_chat(message, fio, stat_tex, phone_number, vps_name, date_)
            # controller.bot.send_message(message.chat.id, f'{fio} {stat_tex} {phone_number} в {vps_name} - {date_}') # -- вывод сообщ на экран телеф
            view.start_menu(message)

vps_dict = read_db()
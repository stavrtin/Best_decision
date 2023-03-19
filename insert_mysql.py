#!/usr/bin/python
# -*- coding: utf8 -*-
#!/usr/bin/python
# -*- coding: utf-8 -*-


# Импортируем библиотеки
from pprint import  pprint
import mysql.connector
from mysql.connector import Error

parse_data = [{"_id": "SBR013-2204180006-0-7", "name_lot": "Самоходная машина и другие виды техники - рулонозамотчик U25, 1990 г.в., заводской № машины (рамы) SBRF314RC1219025, двигатель № не установлен, коробка передач № не установлен, основной ведущий мост № сведения отсутствуют, цвет синий;\nПресс-подборщик рулонный ПР-1,5, 2007 г.в.", "region_lot": "Вологодская область", "price_lot": 696000, "url_lot": "https://tbankrot.ru/item?id=4574940", "name_firma_lot": "ООО \"СЛАВЯНСКАЯ НОВЬ\"", "tel_organis_lot": "Показать", "mail_organis_lot": "Показать"}, {"_id": "SBR013-2204180006-0-6", "name_lot": "Самоходная машина и другие виды техники - двурядный оборачиватель GE240, 2002 г.в., заводской № машины (рамы) SPM S082400214, двигатель № не установлен, коробка передач № не установлен, основной ведущий мост № сведения отсутствуют, цвет синий;\nПресс-подборщик ПРЛ-150ш, 2010 г.в.", "region_lot": "Вологодская область", "price_lot": 543750, "url_lot": "https://tbankrot.ru/item?id=4574939", "name_firma_lot": "ООО \"СЛАВЯНСКАЯ НОВЬ\"", "tel_organis_lot": "Показать", "mail_organis_lot": "Показать"}]



#  ----- подключаемся к БД ----
login = 'root'
user_password = '..ka'
dbase = 'torgi'

my_db = mysql.connector.connect(
    host='localhost',
    user=login,
    passwd=user_password,
    database=dbase,
    auth_plugin='mysql_native_password'
    )
mycursor = my_db.cursor()

###----
# ------- для удаленного ---------------

server = SSHTunnelForwarder(
    # 'XXX.XXX.XXX.XXX',
    '185.231.155.232',
    ssh_username='root',
    ssh_password='tVvrZX8LfFMQHjh6',
    remote_bind_address=('127.0.0.1', 3306)
    )
server.start()

login = 'parser'
user_password = 'tVvrZX8LfFMQHjh6'
dbase = 'parser'

my_db = pymysql.connect(
    host='127.0.0.1',
    port=server.local_bind_port,
    user=login,
    password=user_password,
    db=dbase,
    cursorclass=pymysql.cursors.DictCursor
)

# ------- для удаленного END ---------------

# ---- готовый запрос на создание таблицы -----
# sql_new_table = "CREATE TABLE IF NOT EXISTS lots (id VARCHAR(100), " \
#                 "name_lot text,  " \
#                 "region_lot varchar(100), " \
#                 "price_lot float,   " \
#                 "url_lot varchar(100), " \
#                 "name_firma_lot varchar(100), " \
#                 "tel_organis_lot varchar(100), " \
#                 "mail_organis_lot varchar(100))"

sql_insert_data = f"INSERT INTO lots (`id`, `name_lot`, `region_lot`, `price_lot`,  `url_lot`, `name_firma_lot`,`tel_organis_lot`, `mail_organis_lot`)" \
                      f" VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

# ----- вставляем данные в БД ----
for item in parse_data:
    mycursor.execute(sql_insert_data, (list(item.values())))
    my_db.commit()

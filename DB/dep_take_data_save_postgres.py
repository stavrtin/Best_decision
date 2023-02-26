# Импортируем библиотеки
from pprint import  pprint
from datetime import time, date, datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
# import mysql.connector
import psycopg2

# -----------------------------удалить при боевой работе -----
from test import test_parse_data


def take_name(url):
    ''' Получение имен героев (список)'''

    #  ~~~~~~~ нужно собрать имена героев в список
    driver.get(url)
    # ----- определим количество героев ----
    heroes_object =  driver.find_elements(By.XPATH, "//div[@class='hero-grid']/a")
    # count_heroes = len(heroes_object)

    # ---- возбмем имена героев ----
    list_name_heroes = []
    for hero_ in heroes_object:
        name_hero = hero_.get_attribute('href').split('/')[-1:][0]
        list_name_heroes.append(name_hero)

    return list_name_heroes

def take_list_data(name, pach):
    '''  Собираем данные о противниках игрока. на выходе список
    '''

    # url_counteraction_pach = url_hero + '/' + name + '/counters?date=patch_7.31'
    url_counteraction_pach = url_hero + '/' + name + '/counters?date=patch_' + pach
    driver.get(url_counteraction_pach)

    # ----- определим количество героев из таблицы ----
    heroes_table = driver.find_element(By.CLASS_NAME, "sortable")
    heroes_row = heroes_table.find_elements(By.TAG_NAME, "tr")
    curent_name = [name]
    for row_ in heroes_row[1:3]: # -------------------------------------TEST ----удалить "2" для боевой работы--------
        heroes_data = row_.text
        heroes_data_name = " ".join(heroes_data.split('%')[0].split(' ')[:-1])
        heroes_data_power = heroes_data.split('%')[0].split(' ')[-1:][0]
        curent_name.append([heroes_data_name, heroes_data_power])

    return curent_name

def generate_sql_header(header):
    ''' Функция для подготовки строки с перечнем имен героев для
    последующего использования в запросах CREATE TABLE.. и INSERT '''

    second_third = ''
    for i in range(len(header)):
        second_third = second_third + f", {header[i].replace(' ','_').replace('-','_')} FLOAT"

    return second_third

def generate_value_insert(data_enemy, header, header_dict):
    ''' Собираем значения показателей для последующей вставки в INSERT'''

    # ----- заполним нулями строку. Далее в нее по индексу запишем нужные значения-----
    data_power =  [0 for x in range(len(header) + 1)]

    del data_power[0]
    data_power.insert(0, data_enemy[0])

    for item_enemy in data_enemy[1:]:
        # ----- получение индекса текущего героя из словаря хэдер
        try: index_ = header_dict.get(item_enemy[0].replace("'",'').replace(' ','-').lower())
        except: index_ = 1
        del data_power[index_]
        data_power.insert(index_, item_enemy[1])

    return data_power

def geterate_sql_insert(header):
    ''' Формируем текст запроса SQL на вставку данных в таблицу '''

    # ----- взяли данные из заголовка таблицы
    columns = generate_sql_header(header)
    # ----- подготовили название колонок для использования в запросе INSERT ----
    columns_name = ", ".join([x.replace(' ','').replace('FLOAT', '') for x in columns.split(',')[1:]])
    sss = ", ".join(['%s' for _ in range(len(header) + 1)])

    sql_insert = f"INSERT INTO hero_enemy.hero_enemy (name, {columns_name}) VALUES ({sss})"

    return sql_insert



start = datetime.today().replace(microsecond=0)
print(f'Старт программы в {start}'
      f'\n Идет сбор данных с сайта "https://ru.dotabuff.com/heroes" ')

pach = input('Введите версию патча.Например 7.31: ')


# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver = webdriver.Firefox(executable_path='/home/max/PycharmProjects/Hero_03/geckodriver')
driver = webdriver.Firefox(executable_path='/home/max/geckodriver')




#  ---- пройдемся циклом по всем героям, возьмем данные ---

url_hero = 'https://ru.dotabuff.com/heroes'

# ----- получаеи список героев ----
name_list = take_name(url_hero)


hero_enemy_list = []
for hero_ in name_list[:3]: # -------------------TEST ---удалить "2" для боевой работы--------------
    name = hero_
    hero_enemy_list.append(take_list_data(name, pach))

driver.close()

pprint(hero_enemy_list)


# --------ЗАПИСЬ в БД--------------------------------------------------



# parse_data = hero_enemy_list # ----------------------------для боевой работы ------------------
parse_data = test_parse_data


# --- Это имена героев - для формирования ЗАГОЛОВКА таблицы -----
header = [x[0] for x in parse_data]

key_lst = header
value_list = [header.index(x) + 1 for x in header]
header_dict = dict(zip(key_lst, value_list))

#  ----- подключаемся к БД ----
# login = 'root'
# user_password = '123'
# dbase = 'hero_db'
#
# my_db = mysql.connector.connect(
#     host='localhost',
#     user=login,
#     passwd=user_password,
#     database=dbase
#     )
# mycursor = my_db.cursor()


my_db = psycopg2.connect(
  database="hero_db",
  user="postgres",
  password="123",
  host="localhost",
  port="5432"
)


mycursor = my_db.cursor()





# ---- Запрос на удаление предыдущей таблицы -----
sql = "DROP TABLE IF EXISTS hero_enemy.hero_enemy"
mycursor.execute(sql)

# ---- готовый запрос на создание таблицы -----
sql_new_table = f"CREATE TABLE hero_enemy.hero_enemy (name VARCHAR(255) {generate_sql_header(header)})"
mycursor.execute(sql_new_table)


# ----- проходим циклом по данным, собираем значения для вставки в БД ----
for _ in parse_data:
    data_values = (generate_value_insert(_, header, header_dict)) # ----- берем значения ----
    quest_ = geterate_sql_insert(header)


    mycursor.execute(quest_, data_values)
    my_db.commit()


stop = datetime.today().replace(microsecond=0)

print(f'Старт в {start}, стоп в  {stop}')
print(f'Продолжительность ==> {stop - start} сек')
print(f'Собраны данные о {len(hero_enemy_list)} персонажах')

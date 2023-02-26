import pandas as pd
import psycopg2


vps_list = ['Бутово','Дегунино','Ростокино','Куркино','Царицыно']
Butovo = ['Гагарин', 'Леонов', 'Комаров']
Degun = ['Титов', 'Терешкова', 'Крамаренко','Чкалов']

vps_dict = {'Бутово': ['Гагарин', 'Леонов', 'Комаров'],
            'Дегунино': ['Титов', 'Терешкова', 'Крамаренко', 'Чкалов'],
            'Ростокино': ['Титов-p', 'Терешкова-p', 'Крамаренко-p', 'Чкалов-p'],
            'Куркино': ['Титов-k', 'Терешкова-k', 'Крамаренко-k', 'Чкалов-k'],
            'Царицыно': ['Цитов', 'Церешкова', 'ЦКрамаренко', 'ЦЧкалов'],
            'Некрасовка': ['Нитов', 'НТерешкова', 'НКрамаренко', 'НЧкалов'],
            }



my_db = psycopg2.connect(
  database="vps_jur",
  user="postgres",
  password="1234",
  host="localhost",
  port="5432"
)


mycursor = my_db.cursor()



# ---- Запрос на удаление предыдущей таблицы -----
# sql = "DROP TABLE IF EXISTS vps_jur.spisok"
# mycursor.execute(sql)

vps_dict_1 = {}

# ---- готовый запрос на создание таблицы -----
sql_all_rec = f"SELECT DISTINCT VPS_name FROM spisok"
mycursor.execute(sql_all_rec)
result = mycursor.fetchall()
vps_uniq_list = [i[0] for i in result]

print(vps_uniq_list)
for i in vps_uniq_list:
    sql_fio_from_vps = f"SELECT fio FROM spisok " \
                       f"where VPS_name = '{i}'"
    mycursor.execute(sql_fio_from_vps)
    result_fio = mycursor.fetchall()
    fio_list = [j[0] for j in result_fio]
    print(fio_list)
    vps_dict_1.update({i: fio_list})

print(vps_dict_1)


# ---- получим список уникальных ВПС
# vps_all = [i[1] for i in result]
# vps_uniq_list = list(set([i[1] for i in result]))

# ----- заполним словарь списком ФИО, привязанных к нужной ВПС---




# print(vps_uniq_list)
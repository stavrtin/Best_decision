import sqlite3

conn = sqlite3.connect('zavodd.db')
cursor = conn.cursor()

def output_all():
    # ---- вывод всех --------
    cursor.execute('select * from shtat')
    result = cursor.fetchall()
    print(result)

def find_by_id():
    # ---- поиск всех --------
    find_name = 'Иванов'
    cursor.execute(f'select * from shtat  where name like "%{find_name}%"')
    result = cursor.fetchall()
    print(result)

def insert_data(name, tel, prof):
    # ----- добавление записи -----------
    name_ = name
    tel_ = tel
    prof_ = prof
    cursor.execute(f"insert into shtat (name,tel,prof) values ('{name_}','{tel_}','{prof_}')");
    conn.commit()


def delete_by_id():
    # ----- удаление записи -----------
    id_ = 3
    cursor.execute(f"delete from shtat where id = {id_}");
    conn.commit()

def reload_data_by_id():
    # ----- обновить записи -----------
    id_ = 2
    name_ = 'Комаров'
    tel_ = '4345215'
    prof_ = 'актер'
    cursor.execute(
                   f"update shtat set name = '{name_}', tel = '{tel_}', prof = '{prof_}' where id = {id_}"
                   # f"update shtat set name = '{name_}' where id = {id_}"
                   )
    conn.commit()

# output_all()
# reload_data_by_id()
# name = 'ererer'
# tel = '11111'
# prof = 'fffff'
insert_data(name, tel, prof)
output_all()
# conn.close()

# [(1, 'Петров', 23234, 'водитель'),
# (2, 'Иванов', 12312, 'шеф'),
# (4, 'Сидоров', 333445, 'учитель'),
# (5, 'Козлов', 1111333445, 'директор')]

